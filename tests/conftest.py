import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from main import app
from db.base import Base

from config.settings import settings
from services.user_service import create_user
from models.schemas.users import UserRegister

if not settings.TEST_DATABASE_URL:
    raise Exception("TEST_DATABASE_URL is not configured")

engine = create_engine(settings.TEST_DATABASE_URL)

TestingSessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)

@pytest.fixture
def client():
    return TestClient(app)

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

@pytest.fixture
def user_in_db(db_session, user_data):
    success, user, message = create_user(db_session, UserRegister(**user_data))
    assert success is True
    return user

@pytest.fixture
def auth_token(client, user_data):
    client.post("/api/v1/users/register", json=user_data)

    response = client.post("/api/v1/users/login", json={
        "email": user_data["email"],
        "password": user_data["password"]
    })

    assert response.status_code == 200

    return response.json()["access_token"]

@pytest.fixture
def auth_headers(auth_token):
    return {
        "Authorization": f"Bearer {auth_token}"
    }

def test_get_profile(client, auth_headers):
    response = client.get("/api/v1/users/me", headers=auth_headers)

    assert response.status_code == 200