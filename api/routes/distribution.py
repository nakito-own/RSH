from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Dict
from services.db_service import get_session
from services.distribution_service import get_addresses_with_robots

router = APIRouter()

@router.get("/distribution", response_model=List[Dict])
async def get_distributions(db: Session = Depends(get_session)):
    try:
        addresses_with_robots = get_addresses_with_robots(db)
        return addresses_with_robots
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
