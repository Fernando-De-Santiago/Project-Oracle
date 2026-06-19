from sqlalchemy.orm import Session
from sqlalchemy import select

from models.db.user import Users
from models.schemas.users import UserRegister, UserLogin

from bcrypt import hashpw, gensalt, checkpw


# ---------------- CREATE USER ----------------

def create_user(db: Session, user_data: UserRegister):
    existing_email = db.execute(
        select(Users).where(Users.email == user_data.email)
    ).scalar_one_or_none()

    if existing_email:
        return False, None, "Email already in use"

    existing_username = db.execute(
        select(Users).where(Users.username == user_data.username)
    ).scalar_one_or_none()

    if existing_username:
        return False, None, "Username already in use"

    password_hash = hashpw(
        user_data.password.encode("utf-8"),
        gensalt()
    ).decode("utf-8")

    new_user = Users(
        username=user_data.username,
        email=user_data.email,
        password_hash=password_hash
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return True, new_user, "User created successfully"


# ---------------- AUTHENTICATE USER ----------------

def authenticate_user(db: Session, user_data: UserLogin):
    user = db.execute(
        select(Users).where(Users.email == user_data.email)
    ).scalar_one_or_none()

    if not user:
        return False, None, "Invalid email or password"

    password_valid = checkpw(
        user_data.password.encode("utf-8"),
        user.password_hash.encode("utf-8")
    )

    if not password_valid:
        return False, None, "Invalid email or password"

    return True, user, "Authentication successful"