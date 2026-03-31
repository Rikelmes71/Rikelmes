from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseModel):
    database_url: str = os.getenv("DATABASE_URL", "")
    app_secret_key: str = os.getenv("APP_SECRET_KEY", "")
    encryption_key_base64: str = os.getenv("ENCRYPTION_KEY_BASE64", "")
    microsoft_tenant_id: str = os.getenv("MICROSOFT_TENANT_ID", "")
    microsoft_client_id: str = os.getenv("MICROSOFT_CLIENT_ID", "")
    microsoft_client_secret: str = os.getenv("MICROSOFT_CLIENT_SECRET", "")
    whatsapp_provider: str = os.getenv("WHATSAPP_PROVIDER", "business_api")
    whatsapp_base_url: str = os.getenv("WHATSAPP_BASE_URL", "")
    whatsapp_token: str = os.getenv("WHATSAPP_TOKEN", "")


settings = Settings()
