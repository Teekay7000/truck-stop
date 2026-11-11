from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title = "Truck Stop Api",
    description = "Backend system for our South African Truck Stop Network",
    version = "1.0.0"
)

@app.get("/")
def home():
    return{
        "message":"Welcome to the Truck Stop API" 
    }


class TruckStopCreate(BaseModel):
    name: str
    town: str
    parking_capacity: int

@app.post("/truck-stops")
def create_truck_stop(truck_stop: TruckStopCreate):
    return{
        "message": "Truck stop received successfully",
        "truck_stop":truck_stop
    }


        




