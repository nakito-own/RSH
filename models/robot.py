from sqlalchemy import Column, Integer, String, Boolean
from services.db_service import Base

class Robot(Base):
    __tablename__ = "robots"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(45), nullable=False)
    storage = Column(String(55), nullable=False, default='disabled')
    generation = Column(String(45), nullable=False)
    blockers = Column(Boolean, nullable=False, default=False)
    delivery = Column(Boolean, nullable=False, default=False)
