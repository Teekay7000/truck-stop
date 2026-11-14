
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException

from app.database import engine, Base, SessionLocal
from app import models


# Creates a database session for each request
# and closes it afterwards.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI(
    title="Truck Stop Api",
    description="Backend system for our South African Truck Stop Network",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {
        "message": "Welcome to the Truck Stop API"
    }


class TruckStopCreate(BaseModel):
    name: str
    town: str
    parking_capacity: int

class TruckStopUpdate(BaseModel):
    name: str
    town:str
    parking_capacity: int


@app.post("/truck-stops")
def create_truck_stop(
    truck_stop: TruckStopCreate,
    db: Session = Depends(get_db)
):
    new_truck_stop = models.TruckStop(
        name=truck_stop.name,
        town=truck_stop.town,
        parking_capacity=truck_stop.parking_capacity
    )

    db.add(new_truck_stop)
    db.commit()
    db.refresh(new_truck_stop)

    return {
        "message": "Truck stop created successfully",
        "truck_stop": new_truck_stop
    }

@app.get("/truck-stops")
def get_trucks_stops(db: Session = Depends(get_db)):
    truck_stops = db.query(models.TruckStop).all()

    return truck_stops

@app.get("/truck-stops/{truck_stop_id}")
def get_truck_stop(
    truck_stop_id: int,
    db: Session = Depends(get_db)
):
    truck_stop = db.query(models.TruckStop).filter(
        models.TruckStop.id == truck_stop_id
    ).first()

    if truck_stop is None:
        raise HTTPException(
            status_code=404,
            detail="Truck stop not found"
        )

    return truck_stop


@app.put("/truck-stops/{truck_stop_id}")
def update_truck_stop(
    truck_stop_id : int,
    truck_stop_data : TruckStopUpdate,
    db: Session = Depends(get_db)
):
    truck_stop = db.query(models.TruckStop).filter(
        models.TruckStop.id == truck_stop_id
    ).first()

    if truck_stop is None:
        raise HTTPException(
            status_code = 404,
            detail = "Truck stop not found"
        )
    
    truck_stop.name = truck_stop_data.name
    truck_stop.town = truck_stop_data.town
    truck_stop.parking_capacity = truck_stop_data.parking_capacity

    db.commit()
    db.refresh(truck_stop)

    return {
        "message": "Truck stop updated successfully",
        "truck_stop": truck_stop
    }

@app.delete("/truck-stops/{truck_stop_id}")
def delete_truck_stop(
    truck_stop_id: int,
    db: Session = Depends(get_db)
):
    truck_stop = db.query(models.TruckStop).filter(
        models.TruckStop.id == truck_stop_id
    ).first()

    if truck_stop is None:
        raise HTTPException(
            status_code=404,
            detail="Truck stop not found"
        )

    db.delete(truck_stop)
    db.commit()

    return {
        "message": "Truck stop deleted successfully"
    }


