import pytest
from sqlmodel import Session, SQLModel, create_engine


@pytest.fixture
def test_session():
    engine = create_engine("sqlite://", echo=False)
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session
