"""
Botivate HR Support - Central Configuration
All values are loaded from environment variables / .env file.
Nothing is hardcoded.
"""

from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # --- Application ---
    app_name: str = "Botivate HR Support"
    app_env: str = "development"
    app_secret_key: str = "change-this-to-a-strong-random-secret"
    app_base_url: str = "http://localhost:8000"

    # --- Master Database ---
    database_url: str = "sqlite+aiosqlite:///./botivate_master.db"

    # --- LLM ---
    openai_api_key: str = ""
    openai_model: str = "gpt-4o-mini"

    # --- Fast LLM (Cerebras/Groq for data answers/RAG) ---
    fast_llm_api_key: str = ""
    fast_llm_model: str = ""
    fast_llm_base_url: str = ""

    # --- Google Sheets / OAuth ---
    google_sheet_id: str = ""
    google_service_account_json: str = ""
    google_oauth_client_id: str = ""
    google_oauth_client_secret: str = ""
    google_oauth_redirect_uri: str = "http://localhost:5173/oauth/callback"
    google_employee_sheet_name: str = "RAW DATA"
    google_admin_sheet_name: str = "Admin"

    # --- SMTP Email ---
    smtp_host: str = "smtp.gmail.com"
    smtp_port: int = 587
    smtp_use_tls: bool = True
    smtp_user: str = ""
    smtp_password: str = ""

    # --- JWT Auth ---
    jwt_secret_key: str = "change-this-jwt-secret"
    jwt_algorithm: str = "HS256"
    jwt_expiration_minutes: int = 480

    # --- ChromaDB ---
    chroma_persist_dir: str = "./chroma_data"

    # --- Upload Directories ---
    upload_dir: str = "./uploads"

    # --- Development/Demo Mode ---
    skip_google_auth: bool = False

    def validate_production_secrets(self) -> None:
        """Raise SystemExit if app_env != 'development' and default secrets are used."""
        if self.app_env.lower() != "development":
            errors = []
            if self.app_secret_key == "change-this-to-a-strong-random-secret":
                errors.append("APP_SECRET_KEY is still set to its default value.")
            if self.jwt_secret_key == "change-this-jwt-secret":
                errors.append("JWT_SECRET_KEY is still set to its default value.")
            
            if errors:
                import sys
                print("\n" + "="*80)
                print("❌ PRODUCTION CONFIGURATION ERROR")
                for err in errors:
                    print(f"  - {err}")
                print("Please set strong unique values in your production environment variables.")
                print("="*80 + "\n")
                sys.exit(1)

    class Config:
        env_file = (".env", "../.env")
        env_file_encoding = "utf-8"


settings = Settings()
