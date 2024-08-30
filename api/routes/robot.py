from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional
from services.distribution_service import get_addresses_with_robots
from services.robot_service import add_robot, get_robot, get_all_robots, delete_robot, robot_update
from services.db_service import get_session

router = APIRouter()

class RobotCreateRequest(BaseModel):
    name: str
    storage: str

class RobotUpdateRequest(BaseModel):
    storage: Optional[str] = None
    blockers: Optional[bool] = None
    delivery: Optional[bool] = None

class RobotResponse(BaseModel):
    id: int
    name: str
    storage: str
    generation: str
    blockers: bool
    delivery: bool


@router.get("/robots/")
def get_robots(db: Session = Depends(get_session)):
    robots = get_all_robots(db)
    return [RobotResponse(**robot.__dict__) for robot in robots]

@router.post("/robots/")
def create_robot(request: RobotCreateRequest, db: Session = Depends(get_session)):
    new_robot = add_robot(db, request.name, request.storage)
    return {"message": "Robot created successfully", "robot_id": new_robot.id}


@router.patch("/robots/{id}/")
def update_robot(id: int, request: RobotUpdateRequest, db: Session = Depends(get_session)):
    robot = get_robot(db, id)
    if not robot:
        raise HTTPException(status_code=404, detail="Robot not found")

    updated_robot = robot_update(db, id, **request.dict(exclude_unset=True))

    addresses_with_robots = get_addresses_with_robots(db)

    return {"message": "Robot updated successfully", "addresses_with_robots": addresses_with_robots}


@router.delete("/robots/{id}/")
def remove_robot(id: int, db: Session = Depends(get_session)):
    robot = get_robot(db, id)
    if not robot:
        raise HTTPException(status_code=404, detail="Robot not found")

    delete_robot(db, id)

    return {"message": "Robot deleted successfully"}


@router.get("/robots/stat")
def get_robot_statistics(db: Session = Depends(get_session)):
    robots = get_all_robots(db)

    robots_with_blockers = []
    robots_ready_for_production = []
    robots_in_delivery = []
    other_robots = []

    for robot in robots:
        if robot.blockers and robot.storage != "Аминьевское шоссе, 4А":
            robots_with_blockers.append(RobotResponse(**robot.__dict__))
        elif robot.storage == "Аминьевское шоссе, 4А" and not robot.blockers:
            robots_ready_for_production.append(RobotResponse(**robot.__dict__))
        elif robot.delivery:
            robots_in_delivery.append(RobotResponse(**robot.__dict__))
        else:
            other_robots.append(RobotResponse(**robot.__dict__))

    return {
        "Robots with a blocker on locations": robots_with_blockers,
        "Ready for production": robots_ready_for_production,
        "Robots in delivery": robots_in_delivery,
        "Production": other_robots
    }
