from sqlalchemy import Column, Integer, String
from services.db_service import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nick = Column(String(45), nullable=False)
    name = Column(String(45), nullable=False)
    surname = Column(String(45), nullable=False)
    patronymic = Column(String(45), nullable=False)
    role = Column(String(45), nullable=False)
    avatar = Column(String(45), nullable=False)
