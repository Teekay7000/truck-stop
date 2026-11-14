from sqlalchemy import Column, Integer, String
from app.database import Base

class TruckStop(Base):
    __tablename__ = "truck_stops"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    town = Column(String, nullable=False)
    parking_capacity = Column(Integer, nullable=False)