"""
Auto-setup service for first-time deployment.
Creates company and database connection on first startup.
"""

import os
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.models import Company, DatabaseConnection


async def auto_setup_database(session: AsyncSession):
    """
    Initialize company and database connection if they don't exist.
    Called on every startup - idempotent (safe to run multiple times).
    """
    # Check if company already exists
    result = await session.execute(select(Company).where(Company.id == "company-1"))
    existing_company = result.scalars().first()

    if existing_company:
        print("✅ Database already configured - skipping auto-setup")
        return

    print("🔧 First startup detected - auto-configuring database...")

    try:
        # Create company
        company = Company(
            id="company-1",
            name="Employee Portal",
            industry="Technology",
            hr_name="HR Admin",
            hr_email="hr@company.com",
            support_email="support@company.com",
            google_refresh_token="auto-setup",
            is_active=True
        )
        session.add(company)
        await session.flush()
        print("   ✅ Company created: company-1")

        # Get Google Sheet ID from environment (REQUIRED)
        google_sheet_id = os.getenv("GOOGLE_SHEET_ID", "")
        if not google_sheet_id:
            print("   ⚠️  WARNING: GOOGLE_SHEET_ID not set in .env")
            print("   ⚠️  Database connection will not be created")
            await session.commit()
            return

        # Create database connection
        schema_map = {
            "master_table": "Employee Master Data",
            "primary_key": "Employee ID",
            "phone": "Phone Number",
            "employee_name": "Employee Name",
            "categories": {
                "contact": ["Email", "Phone Number"],
                "job": ["Department", "Designation"],
                "personal": ["Date of Birth", "Gender"]
            }
        }

        db_connection = DatabaseConnection(
            id="db-conn-1",
            company_id="company-1",
            title="Google Sheets - Employee Data",
            description="Employee Master Data from Google Sheets",
            db_type="google_sheets",
            connection_config={
                "spreadsheet_id": google_sheet_id,
                "worksheet": "Employee Master Data"
            },
            schema_map=schema_map,
            is_active=True
        )
        session.add(db_connection)
        await session.commit()
        print("   ✅ Database connection created: db-conn-1")
        print(f"   ✅ Google Sheet ID: {google_sheet_id}")
        print("\n🎉 Auto-setup complete! System is ready to use.")

    except Exception as e:
        await session.rollback()
        print(f"   ❌ Auto-setup failed: {e}")
        raise
