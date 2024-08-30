from sqlalchemy.orm import Session
from models.user import User

def add_user(db: Session, nick: str, name: str, surname: str, patronymic: str, role: str, avatar: str):
    new_user = User(nick=nick, name=name, surname=surname, patronymic=patronymic, role=role, avatar=avatar)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_all_users(db: Session):
    return db.query(User).all()

def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user
