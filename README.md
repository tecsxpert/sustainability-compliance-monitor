# Sustainability Compliance Monitor - Backend

## Overview
This project is a backend system built using Spring Boot to manage user data for sustainability compliance monitoring.

---

##  Tech Stack
- Java 17
- Spring Boot
- PostgreSQL
- Maven

---

## Features
- Create User
- Get All Users
- Update User
- Delete User

---

## API Endpoints

### GET Users
GET /users

### CREATE User
POST /users
{
  "name": "John",
  "email": "john@example.com"
}

### UPDATE User
PUT /users/{id}

### DELETE User
DELETE /users/{id}

---

##  How to Run

1. Go to backend folder:
cd backend

2. Run:
mvn spring-boot:run

3. Open browser:
http://localhost:8080/users

---

## Status
Backend CRUD API working successfully.
