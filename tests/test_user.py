from services.user_service import create_user
from models.schemas.users import UserRegister


def test_sample_user_fixture(user_data):
    assert user_data["email"] == "test@test.com"


def test_create_user_success(db_session, user_data):
    user = UserRegister(**user_data)

    success, new_user, message = create_user(db_session, user)

    assert success is True
    assert new_user.email == user_data["email"]
    assert new_user.username == user_data["username"]
    assert new_user.password_hash != user_data["password"]

def test_duplicate_email_fails(db_session, user_data):
    # First user creation
    create_user(db_session, UserRegister(**user_data))

    # Duplicate email attempt
    duplicate = UserRegister(
        email=user_data["email"],
        username="different_username",
        password=user_data["password"]
    )

    success, user, message = create_user(db_session, duplicate)

    assert success is False
    assert user is None
    assert message == "Email already in use"

def test_duplicate_username_fails(db_session, user_data):
    create_user(db_session, UserRegister(**user_data))

    duplicate = UserRegister(
        email="different@email.com",
        username=user_data["username"],
        password=user_data["password"]
    )

    success, user, message = create_user(db_session, duplicate)

    assert success is False
    assert user is None
    assert message == "Username already in use"