import pytest
from app.agents.hr_agent import (
    get_relevant_table_names,
    compact_record,
    filter_related_records,
    extract_query_identifiers
)

def test_hinglish_table_selection():
    schema_map = {
        "master_table": "RAW DATA",
        "primary_key": "Client Job Code",
        "child_tables": {
            "Steps": {},
            "StepMatrix": {},
            "Steps Directory": {},
            "NEW DASH": {},
            "NEW DASH BANK": {},
            "Status Dash": {},
            "Completed Dash": {},
            "RAW DATA2": {},
            "Query_Master": {},
        }
    }

    # Test "kahan" -> maps to status -> selects Status Dash, NEW DASH, etc.
    res = get_relevant_table_names("HOACPL ka step 7 kahan tak pahuncha", schema_map, "employee")
    assert any(x in res for x in ["Steps", "NEW DASH", "Status Dash"])

    # Test "kitne" -> maps to total -> selects NEW DASH, etc.
    res2 = get_relevant_table_names("total kitne cases pending hain", schema_map, "admin")
    assert any(x in res2 for x in ["NEW DASH", "Status Dash", "Completed Dash"])

    # Test FMS abbreviations: "tev" -> maps to step -> selects Steps, StepMatrix, etc.
    res3 = get_relevant_table_names("tev status update", schema_map, "employee")
    assert any(x in res3 for x in ["Steps", "StepMatrix", "Steps Directory"])


def test_compact_record():
    record = {
        "Client Name": "Agrawal Industries",
        "Client Job Code": "AGR-F25F-TL01",
        "Mobile Number": "9999988888",
        "Unrelated Field": "Ignore Me",
        "FMS1 - Doer": "Danesh",
    }
    
    compacted = compact_record(record)
    assert compacted["Client Name"] == "Agrawal Industries"
    assert compacted["Client Job Code"] == "AGR-F25F-TL01"
    assert compacted["Mobile Number"] == "9999988888"
    assert compacted["FMS1 - Doer"] == "Danesh"
    assert "Unrelated Field" not in compacted


def test_filter_related_records():
    records = [
        {"Client Name": "Agrawal", "Job Code": "AGR01"},
        {"Client Name": "Bansal", "Job Code": "BAN01"},
    ]
    filtered = filter_related_records(records, ["Agrawal"])
    assert len(filtered) == 1
    assert filtered[0]["Client Name"] == "Agrawal"


def test_extract_query_identifiers():
    q = 'Show details for client "Bansal Steel"'
    ids = extract_query_identifiers(q)
    assert "Bansal Steel" in ids

    q2 = 'What is status of case BAN-F25F-TL02'
    ids2 = extract_query_identifiers(q2)
    assert "BAN-F25F-TL02" in ids2
