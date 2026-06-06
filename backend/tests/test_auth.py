"""
Auth tests — JWT round-trip, pure helpers, and the verify-mobile endpoint
(happy path, rejection, and rate limiting).

The Google Sheets adapter and the active-connection DB lookup are stubbed so
these run offline.
"""

import pytest

from app.routers.auth_router import (
    normalize_phone,
    get_first_value,
    verify_admin_password,
)
from app.utils.auth import create_access_token, verify_token


# ── Pure helpers ──────────────────────────────────────────

def test_normalize_phone_strips_formatting():
    assert normalize_phone("+91 98765-43210") == "9876543210"
    assert normalize_phone("(987) 654 3210") == "9876543210"
    assert normalize_phone("  9876543210  ") == "9876543210"


def test_normalize_phone_handles_none():
    assert normalize_phone(None) == ""


def test_get_first_value_case_insensitive():
    record = {"User Name": "alice", "Password": "secret"}
    assert get_first_value(record, ["username", "user name"]) == "alice"
    assert get_first_value(record, ["missing"], default="fallback") == "fallback"


# ── Admin password verification (bcrypt + plaintext fallback) ──

def test_verify_admin_password_plaintext_fallback():
    assert verify_admin_password("secret", "secret") is True
    assert verify_admin_password("secret", "wrong") is False


def test_verify_admin_password_bcrypt():
    import bcrypt
    hashed = bcrypt.hashpw(b"secret", bcrypt.gensalt()).decode("utf-8")
    assert verify_admin_password("secret", hashed) is True
    assert verify_admin_password("wrong", hashed) is False


# ── JWT round-trip ────────────────────────────────────────

def test_jwt_round_trip():
    token = create_access_token({
        "employee_id": "HOACPL-F25F-TL01",
        "employee_name": "Test Client",
        "mobile_number": "9876543210",
        "user_type": "employee",
    })
    payload = verify_token(token)
    assert payload.employee_id == "HOACPL-F25F-TL01"
    assert payload.user_type == "employee"


def test_verify_token_rejects_garbage():
    from fastapi import HTTPException

    with pytest.raises(HTTPException) as exc:
        verify_token("not-a-real-jwt")
    assert exc.value.status_code == 401


# ── verify-mobile endpoint ────────────────────────────────

@pytest.fixture
def stub_auth(monkeypatch):
    """Stub get_active_connection + get_adapter so verify-mobile runs offline."""
    from app.routers import auth_router

    class StubAdapter:
        async def get_all_records(self, table_name=None):
            return [
                {"Client Job Code": "HOACPL-F25F-TL01",
                 "Client Name": "Hindustan Oil",
                 "Mobile Number": "9876543210"},
            ]

    class StubCompany:
        name = "Test CA Firm"

    class StubConn:
        db_type = "google_sheets"
        connection_config = {"spreadsheet_id": "x"}
        schema_map = {
            "master_table": "RAW DATA",
            "phone": "Mobile Number",
            "primary_key": "Client Job Code",
            "employee_name": "Client Name",
        }

    async def _fake_active_conn(_db):
        return StubCompany(), StubConn()

    async def _fake_get_adapter(*_a, **_k):
        return StubAdapter()

    monkeypatch.setattr(auth_router, "get_active_connection", _fake_active_conn)
    monkeypatch.setattr(auth_router, "get_adapter", _fake_get_adapter)


@pytest.fixture
def reset_limiter():
    """Clear the in-memory rate-limit storage so counts start fresh.

    The limiter is process-global and keys on the (testclient) client IP, so
    requests from earlier tests would otherwise consume this test's budget.
    """
    from app.utils.limiter import limiter

    limiter.reset()
    yield
    limiter.reset()


def test_verify_mobile_happy_path(client, stub_auth, reset_limiter):
    resp = client.post("/api/auth/verify-mobile",
                       json={"mobile_number": "9876543210"})
    assert resp.status_code == 200
    body = resp.json()
    assert body["employee_id"] == "HOACPL-F25F-TL01"
    assert body["user_type"] == "employee"
    assert body["access_token"]


def test_verify_mobile_unknown_number(client, stub_auth, reset_limiter):
    resp = client.post("/api/auth/verify-mobile",
                       json={"mobile_number": "0000000000"})
    assert resp.status_code == 401


def test_verify_mobile_rate_limited(client, stub_auth, reset_limiter):
    """6th request within the window must be rejected with 429."""
    codes = [
        client.post("/api/auth/verify-mobile",
                    json={"mobile_number": "0000000000"}).status_code
        for _ in range(6)
    ]
    assert codes[-1] == 429
    assert codes[:5] == [401, 401, 401, 401, 401]
