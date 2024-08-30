from sqlalchemy.orm import Session
from typing import List, Dict
from models.robot import Robot
from models.address import Address


def get_addresses_with_robots(db: Session) -> List[Dict]:
    addresses = db.query(Address).all()

    robots = db.query(Robot).all()

    storage_to_robots: Dict[str, List[Robot]] = {}
    for robot in robots:
        if robot.storage not in storage_to_robots:
            storage_to_robots[robot.storage] = []
        storage_to_robots[robot.storage].append(robot)

    addresses_with_robots = []
    for address in addresses:
        address_data = {
            "id": address.id,
            "storage": address.storage,
            "coordinates": address.coordinates,
            "location": address.location,
            "client": address.client,
            "hub": address.hub,
            "min_robots": address.min_robots,
            "max_robots": address.max_robots,
            "robot_count": address.robot_count,
            "robots": [
                {
                    "id": robot.id,
                    "name": robot.name,
                    "storage": robot.storage,
                    "generation": robot.generation,
                    "blockers": robot.blockers,
                    "delivery": robot.delivery
                } for robot in storage_to_robots.get(address.storage, [])
            ]
        }
        addresses_with_robots.append(address_data)

    return addresses_with_robots
