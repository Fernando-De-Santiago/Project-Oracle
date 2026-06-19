from config.settings import Settings
from models.db.user import Users
from jose import jwt
from jose.exceptions import ExpiredSignatureError, JWTError
from datetime import datetime, timedelta, timezone
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends
from db.session import get_db
from sqlalchemy.orm import Session
settings=Settings()
security_schema=HTTPBearer()

def create_token(user: Users):
    payload={"sub": str(user.user_id), "username": user.username, "exp" :datetime.now(timezone.utc)+timedelta(minutes=settings.JWT_EXPIRE_MINUTES)}
    token = jwt.encode(payload,settings.JWT_SECRET_KEY,algorithm=settings.JWT_ALGORITHM)
    return token

def decode_token(token:str):
    decode_payload = jwt.decode(token,settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])

    return decode_payload

def verify_token(token:str):
    try:
        verified_token=decode_token(token)
        return verified_token
    except (ExpiredSignatureError, JWTError):
        return None
    
def get_current_user(db:Session=Depends(get_db),credentials: HTTPAuthorizationCredentials = Depends(security_schema)):
    token=credentials.credentials
    payload=decode_token(token)
    if payload is None:
        return None
    user_id=payload.get("sub")
    if user_id is None:
        return None
    user=db.get(Users,int(user_id))
    if user is None:
        return None
    return user