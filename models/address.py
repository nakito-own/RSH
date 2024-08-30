from sqlalchemy import Column, Integer, String
from services.db_service import Base

class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    storage = Column(String(255), nullable=False)
    coordinates = Column(String(45), nullable=False)
    location = Column(String(45))
    client = Column(String(45), nullable=False)
    hub = Column(String(45), nullable=False)
    min_robots = Column(Integer)
    max_robots = Column(Integer)
    robot_count = Column(Integer, nullable=False)
