from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from services.address_service import add_address, get_address, get_all_addresses, delete_address, update_address
from services.db_service import get_session
from models.address import Address

router = APIRouter()
class AddressCreateRequest(BaseModel):
    storage: str
    coordinates: str
    location: str = None
    client: str
    hub: str
    min_robots: int = None
    max_robots: int = None
    robot_count: int

class AddressUpdateRequest(BaseModel):
    storage: str = None
    coordinates: str = None
    location: str = None
    client: str = None
    hub: str = None
    min_robots: int = None
    max_robots: int = None
    robot_count: int = None

@router.post("/addresses/")
def create_address(request: AddressCreateRequest, db: Session = Depends(get_session)):
    new_address = add_address(
        db,
        request.storage,
        request.coordinates,
        request.location,
        request.client,
        request.hub,
        request.min_robots,
        request.max_robots,
        request.robot_count
    )
    return {"message": "Address created successfully", "address_id": new_address.id}

@router.get("/addresses/{id}/")
def read_address(id: int, db: Session = Depends(get_session)):
    address = get_address(db, id)
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    return address

@router.get("/addresses/")
def read_all_addresses(db: Session = Depends(get_session)):
    addresses = get_all_addresses(db)
    return addresses

@router.delete("/addresses/{id}/")
def remove_address(id: int, db: Session = Depends(get_session)):
    address = get_address(db, id)
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    delete_address(db, id)
    return {"message": "Address deleted successfully"}

@router.patch("/addresses/{id}/")
def update_address_route(id: int, request: AddressUpdateRequest, db: Session = Depends(get_session)):
    address = get_address(db, id)
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")

    updated_address = update_address(
        db,
        address,
        storage=request.storage,
        coordinates=request.coordinates,
        location=request.location,
        client=request.client,
        hub=request.hub,
        min_robots=request.min_robots,
        max_robots=request.max_robots,
        robot_count=request.robot_count
    )
    return {"message": "Address updated successfully", "address": updated_address}

@router.get("/storages/")
def get_all_storages(db: Session = Depends(get_session)):
    storages = db.query(Address.storage).all()
    return [storage[0] for storage in storages]