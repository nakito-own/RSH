from sqlalchemy.orm import Session
from models.address import Address

def add_address(db: Session, storage: str, coordinates: str, location: str, client: str, hub: str, min_robots: int, max_robots: int, robot_count: int):
    new_address = Address(storage=storage, coordinates=coordinates, location=location, client=client, hub=hub, min_robots=min_robots, max_robots=max_robots, robot_count=robot_count)
    db.add(new_address)
    db.commit()
    db.refresh(new_address)
    return new_address

def get_address(db: Session, address_id: int):
    return db.query(Address).filter(Address.id == address_id).first()

def get_all_addresses(db: Session):
    return db.query(Address).all()

def delete_address(db: Session, address_id: int):
    address = db.query(Address).filter(Address.id == address_id).first()
    if address:
        db.delete(address)
        db.commit()
    return address

def update_address(db: Session, address: Address, storage: str = None, coordinates: str = None, location: str = None, client: str = None, hub: str = None, min_robots: int = None, max_robots: int = None, robot_count: int = None) -> Address:
    if storage is not None:
        address.storage = storage
    if coordinates is not None:
        address.coordinates = coordinates
    if location is not None:
        address.location = location
    if client is not None:
        address.client = client
    if hub is not None:
        address.hub = hub
    if min_robots is not None:
        address.min_robots = min_robots
    if max_robots is not None:
        address.max_robots = max_robots
    if robot_count is not None:
        address.robot_count = robot_count

    db.commit()
    db.refresh(address)
    return address