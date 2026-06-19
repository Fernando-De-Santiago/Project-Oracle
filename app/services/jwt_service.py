from config.settings import settings
from models.db.user import Users
from jose import jwt
from jose.exceptions import ExpiredSignatureError, JWTError
from datetime import datetime, timedelta, timezone
from sqlalchemy.orm import Session


# ---------------- TOKEN CREATION ----------------

def create_token(user: Users):
    payload = {
        "sub": str(user.user_id),
        "username": user.username,
        "exp": datetime.now(timezone.utc)
        + timedelta(minutes=settings.JWT_EXPIRE_MINUTES)
    }

    return jwt.encode(
        payload,
        settings.JWT_SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM
    )


# ---------------- TOKEN DECODING ----------------

def decode_token(token: str):
    return jwt.decode(
        token,
        settings.JWT_SECRET_KEY,
        algorithms=[settings.JWT_ALGORITHM]
    )


# ---------------- TOKEN VALIDATION ----------------

def verify_token(token: str):
    try:
        return decode_token(token)
    except (ExpiredSignatureError, JWTError):
        return None


# ---------------- USER RESOLUTION ----------------

def get_current_user_from_token(db: Session, token: str):
    payload = verify_token(token)

    if not payload:
        return None

    user_id = payload.get("sub")

    if not user_id:
        return None

    return db.get(Users, int(user_id))