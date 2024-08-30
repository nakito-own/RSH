from sqlalchemy.orm import Session
from models.robot import Robot

def add_robot(db: Session, name: str, storage: str):
    id_part = int(name.split("-")[1])
    generation = 'new' if id_part > 390 else 'old'
    new_robot = Robot(id=id_part, name=name, storage=storage, generation=generation)
    db.add(new_robot)
    db.commit()
    db.refresh(new_robot)
    return new_robot

def get_robot(db: Session, robot_id: int):
    return db.query(Robot).filter(Robot.id == robot_id).first()

def get_all_robots(db: Session):
    return db.query(Robot).all()

def delete_robot(db: Session, robot_id: int):
    robot = db.query(Robot).filter(Robot.id == robot_id).first()
    if robot:
        db.delete(robot)
        db.commit()
    return robot

def robot_update(db: Session, robot_id: int, **kwargs):
    robot = db.query(Robot).filter(Robot.id == robot_id).first()
    if robot:
        for key, value in kwargs.items():
            print(f"Setting {key} to {value}")  # Debugging line
            setattr(robot, key, value)
        db.commit()
        db.refresh(robot)
    return robot

