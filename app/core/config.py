import logging
from functools import lru_cache

from pydantic import ValidationError, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

logger = logging.getLogger(__name__)

DEFAULT_ALLOWED_ORIGINS = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1",
    "http://127.0.0.1:8000",
    "https://dariero.github.io",
]


class Settings(BaseSettings):
    database_url: str = "sqlite:///./lumairej.db"  # Development default
    debug: bool = False
    allowed_origins: list[str] = DEFAULT_ALLOWED_ORIGINS

    @field_validator("allowed_origins", mode="before")
    @classmethod
    def parse_allowed_origins(cls, v: str | list[str] | None) -> list[str]:
        """Parse comma-separated string into list of origins and validate format."""
        if v is None:
            return DEFAULT_ALLOWED_ORIGINS
        if isinstance(v, str):
            origins = [origin.strip() for origin in v.split(",") if origin.strip()]
        else:
            origins = v

        # Validate URL format
        for origin in origins:
            if not (origin.startswith("http://") or origin.startswith("https://")):
                logger.warning("CORS origin '%s' does not start with http:// or https://", origin)

        return origins

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


@lru_cache
def get_settings() -> Settings:
    """Factory function for Settings (testable and cacheable)."""
    try:
        return Settings()
    except ValidationError as exc:
        raise RuntimeError(
            "Configuration error. Check your .env file (see .env.template for reference)."
        ) from exc


# For backwards compatibility and convenience
settings = get_settings()
