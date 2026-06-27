import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.base import Base

from config.settings import settings

if not settings.TEST_DATABASE_URL:
    raise Exception("TEST_DATABASE_URL is not configured")

engine = create_engine(settings.TEST_DATABASE_URL)

TestingSessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)

@pytest.fixture
def db_session():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)

@pytest.fixture
def user_data():
    return {
        "email": "test@test.com",
        "username": "testuser1234",
        "password": "Password12345"
    }

