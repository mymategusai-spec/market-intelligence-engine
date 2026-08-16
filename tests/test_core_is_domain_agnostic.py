"""The core/domain boundary, enforced rather than trusted.

A boundary maintained only by convention erodes under delivery pressure, and the erosion
is invisible until the second domain is attempted — at which point it is expensive. This
test makes the erosion visible immediately.

Matching is done on *identifier parts*, not raw substrings: ``asking_price`` splits to
{asking, price} and must not trip the "ski" rule. Prose in docstrings and comments is
exempt, because explaining what the core deliberately does not know requires naming it.
"""

import io
import json
import os
import re
import tokenize
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORE_DIR = os.path.join(REPO_ROOT, "core")
CORE_SCHEMA_DIR = os.path.join(REPO_ROOT, "schemas", "core")

# Vocabulary that would signal a domain has leaked into the core. Deliberately includes
# terms from the *first* domain, since that is the one most likely to contaminate.
FORBIDDEN_TERMS = frozenset(
    [
        "ski", "skiing", "snowboard", "powder", "piste", "lift", "gondola", "chalet",
        "onsen", "ryokan", "minpaku", "niseko", "hakuba", "myoko", "japan", "japanese",
        "property", "resort", "snow", "snowfall", "lodge", "pension", "guest",
    ]
)

# Identifiers that are language or stdlib vocabulary rather than domain vocabulary.
# `@property` is a Python builtin decorator and cannot be renamed.
ALLOWED_EXACT_IDENTIFIERS = frozenset(["property"])


def _python_files(directory):
    for dirpath, _dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(".py"):
                yield os.path.join(dirpath, filename)


def _identifiers(source):
    """Yield (identifier, line_number) for every NAME token.

    Comments and string literals are skipped: they are prose, and prose may legitimately
    say "the core does not know what a ski lift is".
    """
    readline = io.StringIO(source).readline
    for token in tokenize.generate_tokens(readline):
        if token.type == tokenize.NAME:
            yield token.string, token.start[0]


def _offending_parts(identifier):
    """Forbidden words inside an identifier, matched as whole underscore-separated parts."""
    if identifier in ALLOWED_EXACT_IDENTIFIERS:
        return []
    parts = [p for p in re.split(r"_+", identifier.lower()) if p]
    return [p for p in parts if p in FORBIDDEN_TERMS]


class TestCoreIsDomainAgnostic(unittest.TestCase):
    def test_core_does_not_import_domains(self):
        """core/ must never depend on domains/. The dependency runs one way only."""
        offenders = []
        pattern = re.compile(r"^\s*(?:from|import)\s+domains", re.MULTILINE)
        for path in _python_files(CORE_DIR):
            with open(path, "r", encoding="utf-8") as handle:
                if pattern.search(handle.read()):
                    offenders.append(os.path.relpath(path, REPO_ROOT))
        self.assertEqual(
            [], offenders,
            "core/ must not import from domains/. Offending files: %s" % offenders,
        )

    def test_core_identifiers_contain_no_domain_vocabulary(self):
        """Domain nouns in core/ identifiers mean an abstraction has leaked.

        The fix is to generalise the concept — a lift is a target of a `location_metric`,
        a gondola is a `market_catalyst` — not to add an exception here.
        """
        offenders = []
        for path in _python_files(CORE_DIR):
            with open(path, "r", encoding="utf-8") as handle:
                source = handle.read()
            for identifier, line_number in _identifiers(source):
                for part in _offending_parts(identifier):
                    offenders.append(
                        "%s:%d: identifier %r contains domain term %r"
                        % (os.path.relpath(path, REPO_ROOT), line_number, identifier, part)
                    )
        self.assertEqual(
            [], offenders,
            "Domain vocabulary in core/ identifiers:\n  " + "\n  ".join(offenders),
        )

    def test_core_schema_field_names_contain_no_domain_vocabulary(self):
        """Core schema *field names* must stay generic.

        Descriptions may cite domain examples for clarity; the contract itself may not.
        """
        offenders = []
        for filename in sorted(os.listdir(CORE_SCHEMA_DIR)):
            if not filename.endswith(".json"):
                continue
            path = os.path.join(CORE_SCHEMA_DIR, filename)
            with open(path, "r", encoding="utf-8") as handle:
                document = json.load(handle)
            for field_name in _collect_property_names(document):
                for part in _offending_parts(field_name):
                    offenders.append(
                        "%s: field %r contains domain term %r" % (filename, field_name, part)
                    )
        self.assertEqual(
            [], offenders,
            "Domain vocabulary in core schema field names:\n  " + "\n  ".join(offenders),
        )

    def test_domain_modules_may_use_domain_vocabulary(self):
        """Sanity check on the test itself: the rule must apply to core only.

        If this ever fails, the boundary check has been pointed at the wrong tree.
        """
        self.assertTrue(_offending_parts("distance_to_ski_lift"))
        self.assertFalse(_offending_parts("asking_price"))
        self.assertFalse(_offending_parts("location_metric"))


def _collect_property_names(node, names=None):
    """Recursively collect declared field names from a JSON Schema document."""
    if names is None:
        names = []
    if isinstance(node, dict):
        properties = node.get("properties")
        if isinstance(properties, dict):
            names.extend(properties.keys())
        for key, value in node.items():
            # Skip free-text fields; only structural keys carry field names.
            if key in ("description", "title", "examples", "enum"):
                continue
            _collect_property_names(value, names)
    elif isinstance(node, list):
        for item in node:
            _collect_property_names(item, names)
    return names


if __name__ == "__main__":
    unittest.main()
