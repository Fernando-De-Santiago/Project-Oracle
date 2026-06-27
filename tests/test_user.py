from services.user_service import create_user
from models.schemas.users import UserRegister

def test_sample_user_fixture(user_data):
    assert user_data["email"] == "test@test.com"

def test_create_user_success(db_session):
    user=UserRegister(
        email="test@test.com",
        username="testuser1234",
        password="Password12345"
    )
    success, new_user, message = create_user(db_session,user)
    assert success is True
    assert new_user.email == "test@test.com"
    assert new_user.username == "testuser1234"

    assert new_user.password_hash != "Password12345"

def test_duplicate_email_fails(db_session):
    user=UserRegister(
        email="test@test.com",
        username="testuser1234",
        password="Password12345"
    )
    first_success, first_new_user, first_message = create_user(db_session,user)
    assert first_success is True
    assert first_new_user is not None
    duplicate_email=UserRegister(
        email="test@test.com",
        username="testuser12345",
        password="Password12345"
    )
    second_success, second_new_user, second_message = create_user(db_session,duplicate_email)
    assert second_success is False
    assert second_new_user is None
    assert second_message == "Email already in use"

def test_duplicate_username_fails(db_session):
    user=UserRegister(
        email="test@test.com",
        username="testuser1234",
        password="Password12345"
    )
    first_success, first_new_user, first_message = create_user(db_session,user)
    assert first_success is True
    assert first_new_user is not None
    duplicate_username=UserRegister(
        email="test1@test.com",
        username="testuser1234",
        password="Password12345"
    )
    second_success, second_new_user, second_message = create_user(db_session,duplicate_username)
    assert second_success is False
    assert second_new_user is None
    assert second_message == "Username already in use"
   
   