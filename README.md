# South African Truck Stop Network

## Overview

The South African Truck Stop Network is a technology platform aimed at connecting trucking companies, truck drivers and truck-stop facility operators across South Africa.

The platform aims to make it easier for drivers to discover secure truck-stop facilities, access available services and eventually make parking reservations.

## Project Objectives

- Connect truck drivers with secure truck-stop facilities.
- Allow facility operators to register and manage their facilities.
- Enable trucking companies to find facilities for their drivers.
- Provide information about parking capacity and available facilities.
- Support future booking and availability management.

## Technology Stack

- **Backend:** Python, FastAPI
- **Data Validation:** Pydantic
- **Database:** PostgreSQL (planned)
- **Authentication:** Firebase (planned)

## Current Development Progress

The initial backend has been created.

Implemented:
- FastAPI application setup.
- API welcome endpoint.
- Pydantic request model for truck-stop registration.
- POST endpoint for receiving truck-stop information.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Returns the API welcome message |
| POST | `/truck-stops` | Receives truck-stop registration information |

## Running the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/Teekay7000/truck-stop.git
```

### 2. Navigate into the project

```bash
cd truck-stop
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install fastapi uvicorn
```

### 6. Start the development server

```bash
uvicorn app.main:app --reload
```

### 7. Access the API

- API: http://127.0.0.1:8000/
- Interactive API documentation: http://127.0.0.1:8000/docs

## Future Development

- PostgreSQL database integration.
- Persistent truck-stop facility registration.
- Facility management.
- User authentication and authorisation.
- Truck-stop availability management.
- Parking reservation functionality.
- Fleet and trucking company management.
- Nationwide facility expansion.

## Project Status

**Currently under development.**

This project is being developed incrementally, with a focus on building a scalable backend foundation for a South African truck-stop network.