"""Schema hygiene.

JSON Schema is the canonical contract, so a malformed schema or a dangling $ref is a
break in the contract itself. These checks run without any third-party validator.
"""

import json
import os
import re
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCHEMA_ROOT = os.path.join(REPO_ROOT, "schemas")


def schema_files():
    for dirpath, _dirnames, filenames in os.walk(SCHEMA_ROOT):
        for filename in filenames:
            if filename.endswith(".json"):
                yield os.path.join(dirpath, filename)


class TestSchemas(unittest.TestCase):
    def setUp(self):
        self.paths = list(schema_files())
        self.assertTrue(self.paths, "No schemas found")

    def test_all_schemas_are_valid_json(self):
        for path in self.paths:
            with self.subTest(schema=os.path.relpath(path, REPO_ROOT)):
                with open(path, "r", encoding="utf-8") as handle:
                    json.load(handle)

    def test_all_schemas_declare_id_and_title(self):
        for path in self.paths:
            with self.subTest(schema=os.path.relpath(path, REPO_ROOT)):
                with open(path, "r", encoding="utf-8") as handle:
                    document = json.load(handle)
                self.assertIn("$id", document)
                self.assertIn("title", document)
                self.assertIn("description", document)

    def test_local_refs_resolve_to_existing_files(self):
        """A $ref pointing at a file that does not exist is a broken contract."""
        broken = []
        ref_pattern = re.compile(r'"\$ref"\s*:\s*"([^"#]+)(#[^"]*)?"')
        for path in self.paths:
            directory = os.path.dirname(path)
            with open(path, "r", encoding="utf-8") as handle:
                content = handle.read()
            for target, _fragment in ref_pattern.findall(content):
                if target.startswith("http"):
                    continue
                resolved = os.path.normpath(os.path.join(directory, target))
                if not os.path.exists(resolved):
                    broken.append("%s -> %s" % (os.path.relpath(path, REPO_ROOT), target))
        self.assertEqual([], broken, "Broken $refs: %s" % broken)

    def test_records_requiring_provenance_declare_it(self):
        """Record types that carry evidence must require provenance.

        This is the schema-level expression of the rule that no material value may exist
        without a traceable source.
        """
        must_have_provenance = ["observation.json", "asset.json", "entity.json", "market_catalyst.json"]
        for filename in must_have_provenance:
            path = os.path.join(SCHEMA_ROOT, "core", filename)
            with self.subTest(schema=filename):
                with open(path, "r", encoding="utf-8") as handle:
                    document = json.load(handle)
                self.assertIn("provenance", document.get("required", []))

    def test_no_additional_properties_allowed_on_core_records(self):
        """Closed schemas stop typos silently becoming new fields."""
        exempt = {"common.json"}
        core_dir = os.path.join(SCHEMA_ROOT, "core")
        for filename in os.listdir(core_dir):
            if not filename.endswith(".json") or filename in exempt:
                continue
            with self.subTest(schema=filename):
                with open(os.path.join(core_dir, filename), "r", encoding="utf-8") as handle:
                    document = json.load(handle)
                self.assertEqual(
                    False, document.get("additionalProperties"),
                    "%s should set additionalProperties: false" % filename,
                )


if __name__ == "__main__":
    unittest.main()
