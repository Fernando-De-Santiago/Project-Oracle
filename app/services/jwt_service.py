from config.settings import Settings
from models.db.user import Users
from jose import jwt
from jose.exceptions import ExpiredSignatureError, JWTError
from datetime import datetime, timedelta, timezone

def create_token(user: Users):
    payload={"sub": str(user.user_id), "username": user.username, "exp" :datetime.now(timezone.utc)+timedelta(minutes=Settings.JWT_EXPIRE_MINUTES)}
    token = jwt.encode(payload,Settings.JWT_SECRET_KEY,algorithm=Settings.JWT_ALGORITHM)
    return token

def decode_token(token:str):
    decode_payload = jwt.decode(token,Settings.JWT_SECRET_KEY, algorithms=[Settings.JWT_ALGORITHM])

    return decode_payload

def verify_token(token:str):
    try:
        verified_token=decode_token(token)
        return verified_token
    except (ExpiredSignatureError, JWTError):
        return None
    
    