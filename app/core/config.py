from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path
from urllib.parse import urlparse


class Settings(BaseSettings):
    database_url: str
    debug: bool = False

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()

db_path = urlparse(settings.database_url).path
print(f"[DEBUG] Using database at: {Path(db_path).resolve()}")
