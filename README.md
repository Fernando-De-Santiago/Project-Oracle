# Project Oracle - Event Management API & Authentication Platform

---

# Overview

Project Oracle is a backend REST API application designed to manage user authentication and event records through a structured, layered architecture.

The project was created to develop practical experience with backend engineering concepts including API design, authentication workflows, database management, testing, and software architecture.

The current version provides user registration, authentication using JWT tokens, protected API endpoints, and event record management.

The long-term goal of Project Oracle is to evolve into a security-focused monitoring platform capable of collecting infrastructure events from homelab environments and providing visibility into system activity, security events, and operational issues.

---

# Features

Project Oracle currently supports:

## Authentication

- User registration using email, username, and password
    
- Secure password hashing using bcrypt
    
- User authentication using email and password
    
- JWT token generation using Python-JOSE
    
- Protected routes requiring JWT authentication
    
- Current user retrieval through authenticated requests
    

## Event Management

- Create event records
    
- Retrieve stored events
    
- Search events by ID
    
- Update event information
    
- Delete event records
    
- Support predefined event types through enums
    

## Testing

Implemented test coverage includes:

- User creation
    
- Duplicate email validation
    
- Duplicate username validation
    
- Password hashing verification
    
- Successful login authentication
    
- Invalid password handling
    
- Invalid user authentication handling
    
- JWT token authentication
    
- Protected route authorization
    

---

# Tech Stack

## Backend

- Python
    
- FastAPI
    

## Database

- PostgreSQL
    
- SQLAlchemy ORM
    

## Authentication

- JWT authentication
    
- Python-JOSE
    
- bcrypt password hashing
    

## Configuration

- Pydantic Settings
    
- Environment variable configuration
    

## Testing

- pytest
    
- FastAPI TestClient
    
- SQLAlchemy test database
    

---

# Architecture

Project Oracle follows a layered backend architecture designed to separate responsibilities and maintain scalability.

```
Client
  |
  v
API Layer
  |
  v
Authentication Layer
  |
  v
Service Layer
  |
  v
Database Layer
  |
  v
PostgreSQL
```
___
# Architecture Diagram

The following diagram shows the relationship between the API layer, authentication system, service layer, and database layer.

```mermaid
flowchart TD

    Client[Client / API Consumer]

    Client --> API[FastAPI API Layer]

    API --> Auth[Authentication Layer]
    API --> Services[Service Layer]

    Auth --> JWT[JWT Service]
    Auth --> UserDB[(User Database)]

    Services --> UserService[User Service]
    Services --> EventService[Event Service]

    UserService --> DB[(PostgreSQL)]
    EventService --> DB

    DB --> Models[SQLAlchemy Models]
```
---

# API Layer

The API layer defines all HTTP endpoints exposed by the application.

Responsibilities:

- Receive client requests
    
- Validate incoming data
    
- Return formatted responses
    
- Delegate business logic to services
    

The API layer does not contain business rules or database logic.

---

# Authentication Layer

Authentication is handled using JWT-based authentication.

The authentication workflow:

## Registration

1. User submits registration information
    
2. Password is hashed using bcrypt
    
3. User information is stored in PostgreSQL
    

## Login

1. User submits email and password
    
2. Password hash is verified
    
3. JWT token is generated using Python-JOSE
    
4. Client receives an access token
    

## Protected Routes

1. Client sends JWT token through the Authorization header
    
2. FastAPI authentication dependency validates the token
    
3. User identity is extracted from the token payload
    
4. The request proceeds if authentication succeeds
    

---

# Service Layer

The service layer contains the application's business logic.

Responsibilities:

- User creation
    
- User authentication
    
- Password verification
    
- JWT token creation and validation
    
- Event management operations
    

This separation keeps business rules independent from API request handling.

---

# Database Layer

The database layer manages communication between the application and PostgreSQL.

Responsibilities:

- Database engine configuration
    
- Session management
    
- Data persistence
    
- CRUD operations
    

SQLAlchemy is used as the ORM to interact with database models.

---

# Project Structure

```
app/
│
├── api/
│   ├── user.py              # User authentication routes
│   └── events.py            # Event management routes
│
├── config/
│   └── settings.py          # Application configuration
│
├── db/
│   ├── base.py              # SQLAlchemy base model
│   ├── engine.py            # Database engine
│   └── session.py           # Database sessions
│
├── dependencies/
│   └── auth.py              # Authentication dependencies
│
├── models/
│   ├── db/                  # SQLAlchemy database models
│   ├── schemas/             # Pydantic request/response schemas
│   └── core/                # Shared enums and constants
│
├── services/
│   ├── user_service.py      # User business logic
│   ├── jwt_service.py       # JWT handling
│   └── event_service.py     # Event business logic
│
└── main.py                  # FastAPI application entry point
```

---

# API Endpoints

## Register User

**POST**

```
/api/v1/users/register
```

Request:

```json
{
  "email": "user@example.com",
  "username": "exampleuser",
  "password": "Password12345"
}
```

Response:

```json
{
  "user_id": 1,
  "username": "exampleuser",
  "email": "user@example.com",
  "created_at": "2026-01-01T00:00:00"
}
```

---

## Login

**POST**

```
/api/v1/users/login
```

Request:

```json
{
  "email": "user@example.com",
  "password": "Password12345"
}
```

Response:

```json
{
  "access_token": "jwt_token_here",
  "token_type": "bearer"
}
```

---

## Get Current User

**GET**

```
/api/v1/users/me
```

Headers:

```
Authorization: Bearer <access_token>
```

Response:

```json
{
  "user_id": 1,
  "username": "exampleuser",
  "email": "user@example.com",
  "created_at": "2026-01-01T00:00:00"
}
```

---

## Create Event

**POST**

```
/api/v1/events/
```

Request:

```json
{
  "event_type": "LOGIN_FAILED",
  "source": "SERVER01",
  "message": "Failed login attempt detected"
}
```

Response:

```json
{
  "event_id": 1,
  "created_at": "2026-01-01T00:00:00",
  "event_type": "LOGIN_FAILED",
  "source": "SERVER01",
  "message": "Failed login attempt detected"
}
```

---

## Retrieve Events

**GET**

```
/api/v1/events/
```

Response:

```json
[
  {
    "event_id": 1,
    "created_at": "2026-01-01T00:00:00",
    "event_type": "LOGIN_FAILED",
    "source": "SERVER01",
    "message": "Failed login attempt detected"
  }
]
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/Fernando-De-Santiago/Project-Oracle.git
```

## 2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

Windows:

```bash
.venv\Scripts\activate
```

Mac/Linux:

```bash
source .venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure Environment Variables

Create a `.env` file:

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/project_oracle
TEST_DATABASE_URL=postgresql://postgres:password@localhost:5432/project_oracle_test

JWT_SECRET_KEY=your_secret_key
JWT_ALGORITHM=HS256
JWT_EXPIRE_MINUTES=60
```

## 5. Run Application

From the application directory:

```bash
uvicorn main:app --reload
```

---

# Environment Variables

|Variable|Description|
|---|---|
|DATABASE_URL|PostgreSQL connection string|
|TEST_DATABASE_URL|PostgreSQL database used for automated testing|
|JWT_SECRET_KEY|Secret key used to sign JWT tokens|
|JWT_ALGORITHM|Algorithm used for JWT encoding|
|JWT_EXPIRE_MINUTES|JWT expiration duration|

---

# Future Improvements

## Security Enhancements

- Implement refresh token support
    
- Add role-based access control (RBAC)
    
- Implement token revocation and blacklist management
    
- Add request auditing
    
- Add IP address tracking
    

---

## Event System Expansion

- Add event severity levels
    
- Add event filtering by type, source, and timestamp
    
- Expand supported event categories
    
- Add automated event generation
    
- Connect external systems for event ingestion
    

---

## Monitoring and Observability

- Collect logs from homelab infrastructure
    
- Integrate SIEM functionality
    
- Add alerting for suspicious activity
    
- Create monitoring dashboards
    
- Analyze authentication and system events
    

---

## Deployment

- Containerize application using Docker
    
- Add CI/CD pipeline
    
- Deploy application to cloud infrastructure
    
- Add production configuration management
    

---

# Final Notes

Project Oracle represents a foundation for building a security-focused backend monitoring platform.

The current implementation demonstrates:

- REST API development
    
- Layered backend architecture
    
- JWT authentication
    
- Secure password handling
    
- Database integration
    
- Automated testing practices
    

Future versions will focus on expanding event collection, monitoring capabilities, and security analysis features.