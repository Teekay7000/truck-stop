# South African Truck Stop Network

## Project Overview

A platform designed to connect trucking companies, truck drivers and truck-stop operators across South Africa.

The platform aims to make it easier to discover truck stops, access facility information and eventually book secure parking.

## Technology Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Git and GitHub

## Current Development Progress

### Backend API

- [x] FastAPI application setup
- [x] PostgreSQL database connection
- [x] SQLAlchemy database configuration
- [x] Truck stop database model
- [x] Automatic database table creation
- [x] Create a truck stop (POST)
- [x] Retrieve all truck stops (GET)
- [x] Retrieve a truck stop by ID (GET)
- [x] Update truck stop information (PUT)
- [x] Delete a truck stop (DELETE)
- [x] Handle truck stops that do not exist using HTTP 404

### Current API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/truck-stops` | Register a truck stop |
| GET | `/truck-stops` | Retrieve all truck stops |
| GET | `/truck-stops/{truck_stop_id}` | Retrieve one truck stop |
| PUT | `/truck-stops/{truck_stop_id}` | Update a truck stop |
| DELETE | `/truck-stops/{truck_stop_id}` | Delete a truck stop |

## Database

PostgreSQL is used as the primary database.

Current table:

- `truck_stops`

Current fields:

- `id`
- `name`
- `town`
- `parking_capacity`

## Running the Application

Activate the virtual environment and run:

```bash
uvicorn app.main:app --reload
```

API documentation:

`http://127.0.0.1:8000/docs`

## Project Status

Backend development is in progress. The initial truck-stop CRUD functionality has been implemented and tested with PostgreSQL.