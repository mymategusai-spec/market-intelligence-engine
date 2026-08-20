#!/usr/bin/env python3
"""Ingestion interface for the MLIT Real Estate Information Library.

Built ahead of credentials so that approval costs no delay: supply
``MLIT_API_KEY`` in the environment (or a git-ignored ``.env``) and this becomes live
with no code change.

Without a key it runs in **unauthenticated mode**, which does not fetch anything. It
reports exactly what is missing and exits cleanly, so the pipeline never silently
produces empty results that could be mistaken for "no transactions".

    python3 scripts/ingestion/mlit_transactions.py --city 15217 --from 2024 --to 2026

No account has been created and no terms accepted. See
``outputs/mlit-api-access-decision.md``.
"""

from __future__ import annotations

import argparse
import json
import os
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, REPO_ROOT)

API_BASE = "https://www.reinfolib.mlit.go.jp/ex-api/external"
KEY_ENV = "MLIT_API_KEY"

#: Municipality codes for the candidate markets. Used to scope requests once a key exists.
MUNICIPALITY_CODES = {
    "myoko": "15217",
    "yuzawa": "15461",
    "hakuba": "20485",
    "nozawa_onsen": "20561",
    "iiyama": "20213",
    "yamanouchi": "20561",
    "kutchan": "01400",
    "furano": "01229",
}


def load_dotenv(path=None):
    """Read a git-ignored .env without a third-party dependency."""
    path = path or os.path.join(REPO_ROOT, ".env")
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, value = line.partition("=")
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def api_key():
    load_dotenv()
    return os.environ.get(KEY_ENV)


def fetch_transactions(city_code, year_from, year_to, key):
    """Fetch transaction records. Live only once a key exists.

    Deliberately unimplemented beyond the request shape: writing and testing request
    code against an API nobody has agreed terms for would be building on an assumption.
    The shape is recorded so the work is small once approval arrives.
    """
    raise NotImplementedError(
        "Live fetching is intentionally not implemented until owner approval. "
        "Endpoint shape: GET %s/XIT001 with params "
        "{'year': <YYYY>, 'quarter': <1-4>, 'city': <code>} and header "
        "{'Ocp-Apim-Subscription-Key': <key>}. Confirm against the official API manual "
        "at reinfolib.mlit.go.jp/help/apiManual/ before first use." % API_BASE
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--city", default="15217", help="Municipality code, or a name from the built-in map")
    parser.add_argument("--from", dest="year_from", type=int, default=2015)
    parser.add_argument("--to", dest="year_to", type=int, default=2026)
    args = parser.parse_args()

    city = MUNICIPALITY_CODES.get(args.city.lower(), args.city)
    key = api_key()

    print("MLIT Real Estate Information Library - ingestion interface")
    print("=" * 62)
    print("City code : %s" % city)
    print("Years     : %s-%s" % (args.year_from, args.year_to))

    if not key:
        print("Mode      : UNAUTHENTICATED - no data fetched")
        print()
        print("No %s found in the environment or .env." % KEY_ENV)
        print()
        print("This is expected. Registering for the API creates a government account in")
        print("an owner's name and accepts terms of use, which is an owner decision.")
        print("See outputs/mlit-api-access-decision.md.")
        print()
        print("Once a key exists, add it to a git-ignored .env as:")
        print("    %s=your-key-here" % KEY_ENV)
        print("and re-run. No code change is required.")
        return 0

    print("Mode      : AUTHENTICATED")
    try:
        records = fetch_transactions(city, args.year_from, args.year_to, key)
    except NotImplementedError as exc:
        print("\nNot yet implemented:\n  %s" % exc)
        return 1
    print(json.dumps(records[:5], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
