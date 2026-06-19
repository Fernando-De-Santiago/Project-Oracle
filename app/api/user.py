from fastapi import APIRouter, HTTPException, status, Depends
from services.user_event import create_user, authenticate_user
from services.jwt_service import get_current_user, create_token
from models.api.users import UserRegister, UserLogin, UserResponse
from models.api.token import TokenResponse
from sqlalchemy.orm import Session
from sqlalchemy import select
from db.session import get_db

router = APIRouter()

@router.post("/users",response_model=UserResponse, status_code=status.HTTP_201_CREATED)

def create_user_route(user: UserRegister, db: Session = Depends(get_db)):
    success, new_user, message= create_user(db,user)
    if not success:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=message)
    return new_user

@router.post("/login",response_model=TokenResponse, status_code=status.HTTP_200_OK)

def login_user(user:UserLogin, db: Session = Depends(get_db)):
    success, user_login, message = authenticate_user(db, user)
    if not success:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=message)
    token=create_token(user_login)
    return {"token": token}

@router.get("/me")

def get_me(current_user=Depends(get_current_user)):
    return current_user