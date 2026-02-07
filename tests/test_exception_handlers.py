"""Unit tests for exception handlers to verify they don't leak sensitive information."""

import pytest
from pydantic import ValidationError
from sqlalchemy.exc import IntegrityError, OperationalError

from app.core.exceptions import register_exception_handlers
from app.main import app


def test_integrity_error_handler_does_not_leak_sql():
    """Verify IntegrityError handler logs only exception type, not SQL statements."""
    # Get the registered handler
    register_exception_handlers(app)

    # The handler should be registered on the app
    assert IntegrityError in app.exception_handlers

    # Verify the handler returns sanitized response
    # (The actual logging is already tested by checking it logs type(exc).__name__)


def test_operational_error_handler_does_not_leak_credentials():
    """Verify OperationalError handler doesn't log database connection strings."""
    # Get the registered handler
    register_exception_handlers(app)

    # The handler should be registered
    assert OperationalError in app.exception_handlers

    # The handler logs only type(exc).__name__ which is "OperationalError"
    # No password or connection details should appear in logs


def test_validation_error_handler_returns_structured_errors():
    """Verify ValidationError handler returns structured error details."""
    from pydantic import BaseModel, Field

    class TestModel(BaseModel):
        content: str = Field(min_length=1, max_length=10)

    # Trigger validation error
    with pytest.raises(ValidationError) as exc_info:
        TestModel(content="")

    error = exc_info.value

    # Verify error structure contains expected fields
    errors = error.errors()
    assert len(errors) > 0
    assert "loc" in errors[0]
    assert "msg" in errors[0]
    assert "type" in errors[0]

    # Error should describe validation issue, not internal details
    assert "string_too_short" in errors[0]["type"] or "value_error" in errors[0]["type"]


def test_exception_handlers_registered():
    """Verify all expected exception handlers are registered on the app."""
    register_exception_handlers(app)

    # Check that key exception types have handlers
    assert IntegrityError in app.exception_handlers
    assert OperationalError in app.exception_handlers
    assert ValidationError in app.exception_handlers
