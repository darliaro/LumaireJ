import pytest
from sqlmodel import Session, SQLModel, create_engine


@pytest.fixture(scope="function")
def test_session():
    """Create a test database session for each test."""
    engine = create_engine("sqlite://", echo=False)
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session
    engine.dispose()
