from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from services.user_service import add_user, get_user, get_all_users, delete_user
from services.db_service import get_session

router = APIRouter()

class UserCreateRequest(BaseModel):
    nick: str
    name: str
    surname: str
    patronymic: str
    role: str
    avatar: str

@router.post("/users/")
def create_user(request: UserCreateRequest, db: Session = Depends(get_session)):
    new_user = add_user(db, request.nick, request.name, request.surname, request.patronymic, request.role, request.avatar)
    return {"message": "User created successfully", "user_id": new_user.id}

@router.get("/users/{id}/")
def read_user(id: int, db: Session = Depends(get_session)):
    user = get_user(db, id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/users/")
def read_all_users(db: Session = Depends(get_session)):
    users = get_all_users(db)
    return users

@router.delete("/users/{id}/")
def remove_user(id: int, db: Session = Depends(get_session)):
    user = get_user(db, id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    delete_user(db, id)
    return {"message": "User deleted successfully"}
