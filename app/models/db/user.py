from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func
from db.base import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)

    username = Column(String(50), unique=True, index=True, nullable=False)

    email = Column(String(100), unique=True, index=True, nullable=False)

    password_hash = Column(Text, nullable=False)

    created_at = Column(DateTime, server_default=func.now(), nullable=False)