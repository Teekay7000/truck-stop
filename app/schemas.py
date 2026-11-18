
from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict, model_validator


# TRUCK STOP SCHEMAS

class TruckStopCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    town: str = Field(..., min_length=2, max_length=100)
    parking_capacity: int = Field(..., gt=0)


class TruckStopUpdate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    town: str = Field(..., min_length=2, max_length=100)
    parking_capacity: int = Field(..., gt=0)


class TruckStopResponse(BaseModel):
    id: int
    name: str
    town: str
    parking_capacity: int

    model_config = ConfigDict(from_attributes=True)


# FACILITY SCHEMAS

class FacilityCreate(BaseModel):
    truck_stop_id: int = Field(..., gt=0)
    name: str = Field(..., min_length=2, max_length=100)
    available: bool = True


class FacilityResponse(BaseModel):
    id: int
    truck_stop_id: int
    name: str
    available: bool

    model_config = ConfigDict(from_attributes=True)


# BOOKING SCHEMAS

class BookingCreate(BaseModel):
    truck_stop_id: int = Field(..., gt=0)
    driver_id: int | None = Field(default=None, gt=0)
    truck_id: int | None = Field(default=None, gt=0)
    driver_name: str = Field(..., min_length=2, max_length=100)
    truck_registration: str = Field(..., min_length=2, max_length=20)
    arrival_time: datetime
    departure_time: datetime

    @model_validator(mode="after")
    def validate_booking_times(self):
        if self.departure_time <= self.arrival_time:
            raise ValueError("Departure must be after arrival")
        return self


class BookingUpdate(BaseModel):
    arrival_time: datetime
    departure_time: datetime
    status: str = Field(..., pattern="^(pending|confirmed|cancelled)$")

    @model_validator(mode="after")
    def validate_booking_times(self):
        if self.departure_time <= self.arrival_time:
            raise ValueError("Departure must be after arrival")
        return self


class BookingResponse(BaseModel):
    id: int
    truck_stop_id: int
    driver_id: int | None
    truck_id: int | None
    driver_name: str
    truck_registration: str
    arrival_time: datetime
    departure_time: datetime
    status: str

    model_config = ConfigDict(from_attributes=True)


class ParkingAvailabilityResponse(BaseModel):
    truck_stop_id: int
    parking_capacity: int
    booked_spaces: int
    available_spaces: int


# COMPANY SCHEMAS

class CompanyCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=150)
    registration_number: str = Field(..., min_length=2, max_length=50)
    contact_email: str = Field(..., min_length=5, max_length=150)
    phone: str = Field(..., min_length=5, max_length=20)


class CompanyResponse(BaseModel):
    id: int
    name: str
    registration_number: str
    contact_email: str
    phone: str

    model_config = ConfigDict(from_attributes=True)


# DRIVER SCHEMAS

class DriverCreate(BaseModel):
    company_id: int | None = Field(default=None, gt=0)
    full_name: str = Field(..., min_length=2, max_length=100)
    phone: str = Field(..., min_length=5, max_length=20)
    email: str | None = None


class DriverResponse(BaseModel):
    id: int
    company_id: int | None
    full_name: str
    phone: str
    email: str | None

    model_config = ConfigDict(from_attributes=True)


# TRUCK SCHEMAS

class TruckCreate(BaseModel):
    company_id: int | None = Field(default=None, gt=0)
    registration_number: str = Field(..., min_length=2, max_length=20)
    make: str = Field(..., min_length=2, max_length=50)
    model: str = Field(..., min_length=1, max_length=50)


class TruckResponse(BaseModel):
    id: int
    company_id: int | None
    registration_number: str
    make: str
    model: str

    model_config = ConfigDict(from_attributes=True)
