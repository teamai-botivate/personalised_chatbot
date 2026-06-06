"""
Hinglish alias expansion tests for get_relevant_table_names().

Verifies that Romanized-Hindi query words and FMS abbreviations route to the
correct worksheets — the core Phase 0 feature for real users.
"""

import pytest

from app.agents.hr_agent import get_relevant_table_names


SCHEMA = {
    "master_table": "RAW DATA",
    "primary_key": "Client Job Code",
    "child_tables": {
        "Steps": {}, "StepMatrix": {}, "Steps Directory": {},
        "NEW DASH": {}, "NEW DASH BANK": {}, "Status Dash": {},
        "Completed Dash": {}, "RAW DATA2": {}, "Query_Master": {},
        "Sanction Letter": {}, "Post sanction": {}, "FMS2": {},
        "TEAM MEMBER": {},
    },
}


@pytest.mark.parametrize("query,expected_any", [
    # Hinglish status words
    ("HOACPL ka step 7 kahan tak pahuncha", ["Steps", "NEW DASH", "Status Dash"]),
    ("kitne cases pending hain", ["NEW DASH", "Status Dash"]),
    # FMS abbreviations -> step sheets
    ("tev report ka status", ["Steps", "StepMatrix", "Steps Directory"]),
    ("ddr complete hua kya", ["Steps", "StepMatrix"]),
    # Sanction abbreviation
    ("SL aaya kya", ["Sanction Letter", "Post sanction", "FMS2"]),
    # Doer in Hinglish ("kaun")
    ("is case ka doer kaun hai", ["TEAM MEMBER", "FMS2"]),
])
def test_hinglish_routes_to_expected_tables(query, expected_any):
    selected = get_relevant_table_names(query, SCHEMA, "employee")
    assert any(t in selected for t in expected_any), \
        f"{query!r} -> {selected} (expected any of {expected_any})"


def test_word_boundary_avoids_false_positive():
    """'scl' alias must not fire on an unrelated word that merely contains it."""
    # 'muscle' contains 'scl' but should not trigger the step mapping via that alias.
    selected = get_relevant_table_names("muscle pain", SCHEMA, "employee")
    # No step keyword should have matched purely from substring 'scl'.
    assert "StepMatrix" not in selected


def test_empty_query_returns_list():
    assert isinstance(get_relevant_table_names("", SCHEMA, "employee"), list)
