from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

from services.user_service import create_user, authenticate_user
from services.jwt_service import create_token

from dependencies.auth import get_current_user

from models.schemas.users import UserRegister, UserLogin, UserResponse
from models.schemas.token import TokenResponse

from db.session import get_db


router = APIRouter()


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def register_user(user: UserRegister, db: Session = Depends(get_db)):
    success, new_user, message = create_user(db, user)

    if not success:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=message
        )

    return new_user


@router.post(
    "/login",
    response_model=TokenResponse,
    status_code=status.HTTP_200_OK
)
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    success, user_login, message = authenticate_user(db, user)

    if not success:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=message
        )

    token = create_token(user_login)
    return {
    "access_token": token,
    "token_type": "bearer"
}


@router.get("/me", response_model=UserResponse)
def get_me(current_user = Depends(get_current_user)):
    return current_user