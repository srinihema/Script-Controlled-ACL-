#!/usr/bin/env python3
"""Validate the repository's ACL/table configuration files."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load(name):
    with open(ROOT / "config" / name, encoding="utf-8") as f:
        return json.load(f)

def main():
    table = load("table-schema.json")
    roles = load("roles.json")
    acls = load("acls.json")

    assert table["name"] == "u_institution_details"
    assert [c for c in table["fields"] if c["label"] == "Branch"][0]["choices"] == ["ECE", "EEE", "CSE"]

    for role in ("bb1", "bb2", "bb3", "bb4"):
        assert role in roles

    expected = {
        "read": "bb1",
        "create": "bb2",
        "write": "bb3",
        "delete": "bb4",
    }
    actual = {a["operation"]: a["requires_role"] for a in acls}
    assert actual == expected

    read = next(a for a in acls if a["operation"] == "read")
    assert read["data_condition"] == "Branch is EEE"
    assert (ROOT / read["script"]).exists()

    print("Configuration validation passed.")

if __name__ == "__main__":
    main()
