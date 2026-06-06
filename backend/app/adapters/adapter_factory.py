"""
Botivate HR Support - Adapter Factory
Dynamically returns the correct database adapter based on the database type.
New adapters can be plugged in here without modifying any other code.
"""

from typing import Dict, Any
from app.adapters.base_adapter import BaseDatabaseAdapter
from app.adapters.google_sheets_adapter import GoogleSheetsAdapter
from app.models.models import DatabaseType


# ── Registry: map DatabaseType → Adapter Class ────────────
ADAPTER_REGISTRY: Dict[DatabaseType, type] = {
    DatabaseType.GOOGLE_SHEETS: GoogleSheetsAdapter,
    # Future adapters:
    # DatabaseType.POSTGRESQL: PostgreSQLAdapter,
    # DatabaseType.MONGODB: MongoDBAdapter,
    # DatabaseType.SUPABASE: SupabaseAdapter,
    # DatabaseType.EXCEL: ExcelAdapter,
}

from typing import Dict, Any, Optional

# Shared dictionary to store adapter singletons
_adapter_instances: Dict[tuple, BaseDatabaseAdapter] = {}

async def get_adapter(db_type: DatabaseType, connection_config: Dict[str, Any], refresh_token: Optional[str] = None) -> BaseDatabaseAdapter:
    """
    Factory function: returns a connected adapter instance for the given DB type (reused if available).
    """
    adapter_class = ADAPTER_REGISTRY.get(db_type)
    if not adapter_class:
        raise ValueError(f"No adapter registered for database type: {db_type.value}. "
                         f"Supported types: {[t.value for t in ADAPTER_REGISTRY.keys()]}")

    # Generate a unique key based on config
    import json
    config_key = json.dumps(connection_config, sort_keys=True)
    cache_key = (db_type.value, config_key, refresh_token)

    if cache_key in _adapter_instances:
        adapter = _adapter_instances[cache_key]
        # Verify the adapter remains valid
        if hasattr(adapter, "spreadsheet") and adapter.spreadsheet:
            print(f"[ADAPTER FACTORY] ✓ Reusing existing adapter for {db_type.value}")
            return adapter

    print(f"[ADAPTER FACTORY] 🔌 Creating new adapter instance for {db_type.value}")
    adapter = adapter_class()
    await adapter.connect(connection_config, refresh_token=refresh_token)
    _adapter_instances[cache_key] = adapter
    return adapter
