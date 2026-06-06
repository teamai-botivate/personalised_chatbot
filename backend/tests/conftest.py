"""
Shared pytest fixtures for the Finance FMS backend test suite.

These fixtures spin up the FastAPI app with the DB dependency and the
Google Sheets adapter stubbed out, so tests never touch a live database
or the Google Sheets API.
"""

import os

import pytest

# Force development mode so validate_production_secrets() never aborts the
# process during import, regardless of the developer's local .env.
os.environ.setdefault("APP_ENV", "development")


class FakeResult:
    """Mimics the subset of SQLAlchemy Result used by the routers."""

    def __init__(self, value):
        self._value = value

    def scalars(self):
        return self

    def first(self):
        return self._value


class FakeSession:
    """Minimal async DB session stand-in.

    `execute` returns a configurable value so route logic that selects the
    active Company / DatabaseConnection can run without a real database.
    """

    def __init__(self, result_value=None):
        self._result_value = result_value

    async def execute(self, *_args, **_kwargs):
        return FakeResult(self._result_value)

    async def close(self):
        return None


@pytest.fixture
def app():
    """Return the FastAPI app instance (imported lazily to apply env first)."""
    from app.main import app as fastapi_app

    return fastapi_app


@pytest.fixture
def client(app):
    """A TestClient with the DB dependency overridden and lifespan disabled.

    The app's lifespan calls init_db + auto_setup_database against the real
    engine, which we don't want in unit tests. We deliberately construct the
    TestClient WITHOUT the `with` context manager so Starlette never fires the
    startup/shutdown (lifespan) events. The get_db override supplies a fake
    session, so the health route's DB check still exercises real route logic.
    """
    from fastapi.testclient import TestClient
    from app.database import get_db

    async def _fake_get_db():
        yield FakeSession()

    app.dependency_overrides[get_db] = _fake_get_db
    # No `with` block => lifespan startup/shutdown is skipped.
    # raise_server_exceptions=False so 500s come back as responses, not raises.
    test_client = TestClient(app, raise_server_exceptions=False)
    try:
        yield test_client
    finally:
        app.dependency_overrides.clear()
