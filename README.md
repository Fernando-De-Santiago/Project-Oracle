# Project Oracle - Event Management API with JWT Authentication

---

# Overview

Project Oracle is a backend application designed to manage user authentication and event records through a REST API. This project was built to gain experience in backend architecture, authentication workflows, and database-driven applications while creating a foundation for future security-focused event processing.

The long-term goal of Project Oracle is to evolve into a security-focused monitoring platform capable of collecting events from homelab infrastructure and providing visibility into system activity and potential issues.

---

# Features

Project Oracle has the following features:

- Register an account via email, username, and password
- Authenticate users using email and password
- Generate JWT tokens for authenticated users
- Access protected endpoints using JWT authentication
- Create events with event type, source, and message
- Retrieve stored event records
- Update event types and messages
- Delete existing event records

---

# Tech Stack

## Backend

- Python
- FastAPI

## Database

- PostgreSQL
- SQLAlchemy (ORM)

## Authentication

- JWT (Python-JOSE)
- bcrypt (password hashing)

## Configuration

- Pydantic Settings

## Testing

- pytest (future implementation)

---

# Architecture

## API Layer

The API layer is the entry point for all HTTP requests. It defines the routes exposed by the application and maps incoming requests to their corresponding handler functions.

Each route receives request data and delegates business logic to the service layer. The API layer is responsible for request handling and response formatting and does not contain business logic.

---

## Service Layer

The service layer is responsible for handling the core business logic of the application. It processes data received from the API layer, applies validation and business rules, and interacts with the database layer when necessary.

This layer acts as an intermediary between the API layer and the database layer, ensuring that business logic is centralized and separated from request handling concerns.

---

## Database Layer

The database layer is responsible for managing the connection between the application and the database. It uses a database engine to establish and configure this connection.

Database sessions are created per request to handle transactions and ensure proper interaction with the database. This layer is responsible for data persistence, including creating, reading, updating, and deleting records.

It represents the lowest level of the application architecture and does not contain business logic.

---

# Project Structure

The project follows a modular structure designed to separate concerns and improve maintainability.

```
app/
│
├── api/               # API route definitions (FastAPI endpoints)
├── config/            # Application configuration and settings
├── db/                # Database engine and session management
├── models/            # Database models and Pydantic schemas
├── services/          # Business logic layer
├── main.py            # Application entry point
```

---

# Architecture Diagram
```mermaid
flowchart TD

Client[Client] --> API[API Layer]

API --> Service[Service Layer]
Service --> DB[Database Layer]
DB --> Postgres[(PostgreSQL)]

API -->|Handles HTTP Requests| API
Service -->|Business Logic Processing| Service
DB -->|Data Persistence| DB
```
---

# Installation

1. Clone the repository

```
git clone https://github.com/Fernando-De-Santiago/Project-Oracle.git
```

2. Create a virtual environment

```
python -m venv .venv
```

3. Activate the virtual environment

**Windows:**

```
.venv\Scripts\activate
```

**Mac/Linux:**

```
source .venv/bin/activate
```

4. Install dependencies

```
pip install -r requirements.txt
```

5. Run the server from the `/app` directory

```
uvicorn main:app --reload
```

6. Set up environment variables

Create a `.env` file in the root directory and define:

```
DATABASE_URL=postgresql://postgres:YourPassword@localhost:5432/project_oracle
JWT_SECRET_KEY=YourSecretKey
JWT_ALGORITHM=HS256
JWT_EXPIRE_MINUTES=60
```

**Note:** Ensure PostgreSQL is running and the database is accessible before starting the server.

---

# Environment Variables

|Variable|Description|
|---|---|
|DATABASE_URL|PostgreSQL connection string used by SQLAlchemy engine|
|JWT_SECRET_KEY|Secret key used to sign and verify JWT tokens|
|JWT_ALGORITHM|Algorithm used for JWT encoding (HS256 recommended)|
|JWT_EXPIRE_MINUTES|Token expiration time in minutes|

---

# API Usage Examples

## 1. Register User

**POST** `/register`

Request:

```json
{  
   "email": "",  
   "username": "",  
   "password": ""
}
```

Response:

```json
{
  "user_id": 1,  
  "username": "",  
  "email": "",  
  "created_at": ""}
```

---

## 2. Login

**POST** `/login`

Request:

```json
{
  "email": "",  
  "password": ""
}
```

Response:

```json
{
  "token": ""
}
```

---

## 3. Get Current User (Protected Route)

**GET** `/me`

Headers:

```
Authorization: Bearer <token>
```

Response:

```json
{
  "user_id": 1,  
  "username": "",  
  "email": "",  
  "created_at": ""
}
```

---

## 4. Create Event

**POST** `/events`

Request:

```json
{
  "event_type": "",  
  "source": "",  
  "message": ""
}
```

Response:

```json
{
  "event_id": 1,  
  "created_at": "",  
  "event_type": "",  
  "source": "",  
  "message": ""
}
```

---

## 5. Get All Events

**GET** `/events`

Response:

```json
[
  {
      "event_id": 1,    
      "created_at": "",    
      "event_type": "",    
      "source": "",    
      "message": ""  
	}
]
```

---

# Future Improvements

## Security Improvements

- Implement refresh token support for improved session management
- Add role-based access control (RBAC) for user permissions
- Implement token revocation / blacklist mechanism

---

## Event System Expansion

- Introduce severity levels for event classification
- Add filtering capabilities for event queries (by type, source, date)
- Expand supported event types for broader system monitoring
- IP logging for authentication and request tracking
- Event tracking for file uploads
- Event tracking for file downloads

---

## Monitoring / Observability

- Ingest system logs from external sources and services
- Implement real-time alerting for critical events
- Integrate network monitoring tools for enhanced visibility in a homelab environment

---

## Testing & Reliability

- Add unit tests for service layer logic
- Implement integration tests for API endpoints
- Introduce automated API testing using pytest

---

## Deployment

- Containerize application using Docker
- Set up CI/CD pipeline for automated testing and deployment
- Explore cloud deployment options for production readiness

---

# Final Notes

Project Oracle is an evolving backend system designed to demonstrate authentication workflows, API design principles, and layered architecture. Future iterations will focus on expanding observability and transitioning toward a full security monitoring platform for homelab environments.