"""Unit tests for configuration module."""

from app.core.config import Settings


def test_parse_allowed_origins_with_comma_separated_string():
    """Test parsing comma-separated origin strings."""
    settings = Settings(
        database_url="sqlite://", allowed_origins="http://localhost,http://example.com"
    )
    assert settings.allowed_origins == ["http://localhost", "http://example.com"]


def test_parse_allowed_origins_strips_whitespace():
    """Test that whitespace around origins is stripped."""
    settings = Settings(
        database_url="sqlite://", allowed_origins="http://localhost , http://example.com  "
    )
    assert settings.allowed_origins == ["http://localhost", "http://example.com"]


def test_parse_allowed_origins_filters_empty_strings():
    """Test that empty strings are filtered out."""
    settings = Settings(
        database_url="sqlite://", allowed_origins="http://localhost,,http://example.com"
    )
    assert settings.allowed_origins == ["http://localhost", "http://example.com"]


def test_parse_allowed_origins_with_list():
    """Test that list input is passed through."""
    origins = ["http://localhost", "http://example.com"]
    settings = Settings(database_url="sqlite://", allowed_origins=origins)
    assert settings.allowed_origins == origins


def test_parse_allowed_origins_with_none():
    """Test that None returns default origins."""
    settings = Settings(database_url="sqlite://")
    assert "http://localhost" in settings.allowed_origins
    assert "http://localhost:8000" in settings.allowed_origins


def test_database_url_has_default():
    """Test that database_url has a sensible default for development."""
    settings = Settings()
    assert settings.database_url == "sqlite:///./lumairej.db"


def test_debug_defaults_to_false():
    """Test that debug mode is False by default."""
    settings = Settings(database_url="sqlite://")
    assert settings.debug is False
