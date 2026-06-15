from fastapi import APIRouter, HTTPException, status, Depends
from services.user_event import create_user, authenticate_user
from models.api.users import UserRegister, UserLogin, UserResponse
from sqlalchemy.orm import Session
from sqlalchemy import select
from db.session import get_db
from models.db.user import Users

router = APIRouter()

@router.post("/users",response_model=UserResponse, status_code=status.HTTP_201_CREATED)

def create_user_route(user: UserRegister, db: Session = Depends(get_db)):
    success, new_user, message= create_user(db,user)
    if not success:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=message)
    return new_user

@router.post("/users",response_model=UserResponse, status_code=status.HTTP_202_ACCEPTED)

def login_user(user:UserLogin, db: Session = Depends(get_db)):
    success, user_login, message = authenticate_user(db, user)
    if not success:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=message)
    return user_login