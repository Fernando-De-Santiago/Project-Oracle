from models.api.users import UserRegister, UserLogin, UserResponse
from datetime import datetime
from sqlalchemy import select, inspect
from sqlalchemy.orm import Session
from models.db.user import Users
from bcrypt import hashpw, gensalt, checkpw

def create_user(db: Session, user_data:UserRegister):
    check_email = db.query(Users).filter(Users.email == user_data.email).first()
    if check_email:
        return False, None, "Email already in use"
    check_user = db.query(Users).filter(Users.username == user_data.username).first()
    if check_user:
        return False, None, "Username already in use"
    password = user_data.password.encode('utf-8')
    salt = gensalt()
    password_hashed=hashpw(password, salt).decode('utf-8')
    new_user=Users(username=user_data.username, email=user_data.email, password_hash=password_hashed)
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return True,new_user,"Created New User"

def authenticate_user(db: Session, user_data:UserLogin):
    user = db.query(Users).filter(Users.email == user_data.email).first()
    if not user:
        return False, None, "Email is incorrect"
    password_valid = checkpw(user_data.password.encode('utf-8'),user.password_hash.encode('utf-8'))
    if not password_valid:
        return False, None, "Password is incorrect"
    return True, user, "Authentication Successful"