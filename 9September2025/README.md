# Flask API Practice - HTTP Methods (GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS)

This project demonstrates the implementation of all major HTTP methods in Flask, showcasing RESTful API design principles with a user management system.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [HTTP Methods Explained](#http-methods-explained)
- [Example Usage](#example-usage)
- [Testing the API](#testing-the-api)
- [Project Structure](#project-structure)
- [Best Practices Demonstrated](#best-practices-demonstrated)

## 🎯 Overview

This Flask application provides a comprehensive example of implementing all major HTTP methods:
- **GET**: Retrieve data
- **POST**: Create new resources
- **PUT**: Complete resource replacement
- **PATCH**: Partial resource updates
- **DELETE**: Remove resources
- **HEAD**: Get resource metadata (headers only)
- **OPTIONS**: Discover allowed methods and CORS support

The API manages a simple user database with CRUD operations, demonstrating proper RESTful design patterns.

## ✨ Features

- ✅ Complete CRUD operations for user management
- ✅ Proper HTTP status codes and error handling
- ✅ JSON request/response format
- ✅ Input validation and error messages
- ✅ RESTful API design principles
- ✅ In-memory data storage (for demonstration)
- ✅ Comprehensive error handling
- ✅ Detailed API documentation

## 🔧 Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## 📦 Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd /path/to/9September2025
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv flask_env
   source flask_env/bin/activate  # On Windows: flask_env\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Running the Application

1. **Start the Flask server:**
   ```bash
   python app.py
   ```

2. **The server will start on:**
   ```
   http://localhost:5000
   ```

3. **You should see output like:**
   ```
   Starting Flask API Practice Server...
   Available endpoints:
     GET    /           - Welcome message
     GET    /users      - Get all users
     GET    /users/<id> - Get specific user
     POST   /users      - Create new user
     PUT    /users/<id> - Update user completely
     PATCH  /users/<id> - Update user partially
   
   Server will start on http://localhost:5000
   * Running on all addresses (0.0.0.0)
   * Running on http://127.0.0.1:5000
   * Running on http://[::1]:5000
   ```

## 📚 API Documentation

### Base URL
```
http://localhost:5000
```

### Endpoints

#### 1. Welcome Endpoint
- **URL:** `/`
- **Method:** `GET`
- **Description:** Returns welcome message and available endpoints
- **Response:**
  ```json
  {
    "message": "Welcome to Flask API Practice",
    "version": "1.0.0",
        "endpoints": {
            "GET": ["/", "/users", "/users/<id>"],
            "POST": ["/users"],
            "PUT": ["/users/<id>"],
            "PATCH": ["/users/<id>"],
            "DELETE": ["/users/<id>"],
            "HEAD": ["/users", "/users/<id>"],
            "OPTIONS": ["/", "/users", "/users/<id>"]
        }
  }
  ```

#### 2. Get All Users
- **URL:** `/users`
- **Method:** `GET`
- **Description:** Retrieve all users
- **Response:**
  ```json
  {
    "success": true,
    "count": 3,
    "data": [
      {
        "id": 1,
        "name": "John Doe",
        "email": "john@example.com",
        "age": 30,
        "created_at": "2025-01-01T10:00:00Z"
      }
    ]
  }
  ```

#### 3. Get Specific User
- **URL:** `/users/<id>`
- **Method:** `GET`
- **Description:** Retrieve a specific user by ID
- **Parameters:**
  - `id` (integer): User ID
- **Success Response (200):**
  ```json
  {
    "success": true,
    "data": {
      "id": 1,
      "name": "John Doe",
      "email": "john@example.com",
      "age": 30,
      "created_at": "2025-01-01T10:00:00Z"
    }
  }
  ```
- **Error Response (404):**
  ```json
  {
    "success": false,
    "message": "User with ID 999 not found"
  }
  ```

#### 4. Create New User
- **URL:** `/users`
- **Method:** `POST`
- **Description:** Create a new user
- **Request Body:**
  ```json
  {
    "name": "Alice Johnson",
    "email": "alice@example.com",
    "age": 28
  }
  ```
- **Success Response (201):**
  ```json
  {
    "success": true,
    "message": "User created successfully",
    "data": {
      "id": 4,
      "name": "Alice Johnson",
      "email": "alice@example.com",
      "age": 28,
      "created_at": "2025-01-15T14:30:00Z"
    }
  }
  ```
- **Error Responses:**
  - **400:** Missing required fields
  - **409:** Email already exists

#### 5. Update User (Complete Replacement)
- **URL:** `/users/<id>`
- **Method:** `PUT`
- **Description:** Replace entire user resource
- **Request Body:**
  ```json
  {
    "name": "John Updated",
    "email": "john.updated@example.com",
    "age": 31
  }
  ```
- **Success Response (200):**
  ```json
  {
    "success": true,
    "message": "User updated successfully",
    "data": {
      "id": 1,
      "name": "John Updated",
      "email": "john.updated@example.com",
      "age": 31,
      "created_at": "2025-01-01T10:00:00Z",
      "updated_at": "2025-01-15T15:00:00Z"
    }
  }
  ```

#### 6. Update User (Partial Update)
- **URL:** `/users/<id>`
- **Method:** `PATCH`
- **Description:** Update only specified fields
- **Request Body:**
  ```json
  {
    "age": 32
  }
  ```
- **Success Response (200):**
  ```json
  {
    "success": true,
    "message": "User updated successfully. Updated fields: age",
    "data": {
      "id": 1,
      "name": "John Doe",
      "email": "john@example.com",
      "age": 32,
      "created_at": "2025-01-01T10:00:00Z",
      "updated_at": "2025-01-15T15:30:00Z"
    }
  }
  ```

#### 7. Delete User
- **URL:** `/users/<id>`
- **Method:** `DELETE`
- **Description:** Delete a user by ID
- **Parameters:**
  - `id` (integer): User ID
- **Success Response (200):**
  ```json
  {
    "success": true,
    "message": "User with ID 1 deleted successfully"
  }
  ```
- **Error Response (404):**
  ```json
  {
    "success": false,
    "message": "User with ID 999 not found"
  }
  ```

#### 8. Get Headers for All Users
- **URL:** `/users`
- **Method:** `HEAD`
- **Description:** Get response headers without body (same as GET but no content)
- **Response:** Headers only (no body)
- **Use Case:** Check if resource exists, get metadata, check last-modified

#### 9. Get Headers for Specific User
- **URL:** `/users/<id>`
- **Method:** `HEAD`
- **Description:** Get response headers for specific user without body
- **Parameters:**
  - `id` (integer): User ID
- **Response:** Headers only (no body)
- **Use Case:** Check if user exists, get metadata

#### 10. Get Allowed Methods for Home
- **URL:** `/`
- **Method:** `OPTIONS`
- **Description:** Get allowed HTTP methods for home endpoint
- **Response:**
  ```json
  {
    "message": "Available methods for this endpoint",
    "allowed_methods": ["GET", "OPTIONS"]
  }
  ```
- **Headers:** Includes `Allow` and CORS headers

#### 11. Get Allowed Methods for Users
- **URL:** `/users`
- **Method:** `OPTIONS`
- **Description:** Get allowed HTTP methods for users collection
- **Response:**
  ```json
  {
    "message": "Available methods for /users endpoint",
    "allowed_methods": ["GET", "POST", "HEAD", "OPTIONS"],
    "description": {
      "GET": "Retrieve all users",
      "POST": "Create a new user",
      "HEAD": "Get headers only (no body)",
      "OPTIONS": "Get allowed methods"
    }
  }
  ```

#### 12. Get Allowed Methods for Specific User
- **URL:** `/users/<id>`
- **Method:** `OPTIONS`
- **Description:** Get allowed HTTP methods for specific user
- **Parameters:**
  - `id` (integer): User ID
- **Response:**
  ```json
  {
    "message": "Available methods for /users/1 endpoint",
    "allowed_methods": ["GET", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS"],
    "description": {
      "GET": "Retrieve user by ID",
      "PUT": "Update user completely",
      "PATCH": "Update user partially",
      "DELETE": "Delete user",
      "HEAD": "Get headers only (no body)",
      "OPTIONS": "Get allowed methods"
    }
  }
  ```

## 🔍 HTTP Methods Explained

### GET
- **Purpose:** Retrieve data
- **Idempotent:** Yes (safe operation)
- **Body:** No request body
- **Use Case:** Fetching resources

### POST
- **Purpose:** Create new resources
- **Idempotent:** No
- **Body:** JSON data for new resource
- **Use Case:** Adding new items to collection

### PUT
- **Purpose:** Complete resource replacement
- **Idempotent:** Yes
- **Body:** Complete resource data
- **Use Case:** Updating entire resource

### PATCH
- **Purpose:** Partial resource updates
- **Idempotent:** No (in practice)
- **Body:** Only fields to update
- **Use Case:** Modifying specific fields

### DELETE
- **Purpose:** Remove resources
- **Idempotent:** Yes
- **Body:** No request body (usually)
- **Use Case:** Deleting items from collection

### HEAD
- **Purpose:** Get resource metadata (headers only)
- **Idempotent:** Yes (safe operation)
- **Body:** No request body, no response body
- **Use Case:** Check if resource exists, get metadata, check last-modified

### OPTIONS
- **Purpose:** Discover allowed methods and CORS support
- **Idempotent:** Yes (safe operation)
- **Body:** No request body
- **Use Case:** CORS preflight requests, API discovery

## 💡 Example Usage

### Using curl

1. **Get all users:**
   ```bash
   curl -X GET http://localhost:5000/users
   ```

2. **Get specific user:**
   ```bash
   curl -X GET http://localhost:5000/users/1
   ```

3. **Create new user:**
   ```bash
   curl -X POST http://localhost:5000/users \
     -H "Content-Type: application/json" \
     -d '{"name": "Alice Johnson", "email": "alice@example.com", "age": 28}'
   ```

4. **Update user completely (PUT):**
   ```bash
   curl -X PUT http://localhost:5000/users/1 \
     -H "Content-Type: application/json" \
     -d '{"name": "John Updated", "email": "john.updated@example.com", "age": 31}'
   ```

5. **Update user partially (PATCH):**
   ```bash
   curl -X PATCH http://localhost:5000/users/1 \
     -H "Content-Type: application/json" \
     -d '{"age": 32}'
   ```

6. **Delete user:**
   ```bash
   curl -X DELETE http://localhost:5000/users/1
   ```

7. **Get headers only (HEAD):**
   ```bash
   curl -I http://localhost:5000/users
   curl -I http://localhost:5000/users/1
   ```

8. **Get allowed methods (OPTIONS):**
   ```bash
   curl -X OPTIONS http://localhost:5000/
   curl -X OPTIONS http://localhost:5000/users
   curl -X OPTIONS http://localhost:5000/users/1
   ```

### Using Python requests

```python
import requests

base_url = "http://localhost:5000"

# Get all users
response = requests.get(f"{base_url}/users")
print(response.json())

# Create new user
new_user = {
    "name": "Alice Johnson",
    "email": "alice@example.com",
    "age": 28
}
response = requests.post(f"{base_url}/users", json=new_user)
print(response.json())

# Update user partially
update_data = {"age": 29}
response = requests.patch(f"{base_url}/users/4", json=update_data)
print(response.json())

# Delete user
response = requests.delete(f"{base_url}/users/4")
print(response.json())

# Get headers only (HEAD)
response = requests.head(f"{base_url}/users")
print(f"Status: {response.status_code}")
print(f"Headers: {dict(response.headers)}")

# Get allowed methods (OPTIONS)
response = requests.options(f"{base_url}/users")
print(response.json())
```

## 🧪 Testing the API

### Manual Testing
1. Start the Flask server
2. Use the provided curl commands or Python examples
3. Test different scenarios (valid data, invalid data, missing fields)

### Using Postman
1. Import the endpoints into Postman
2. Test each HTTP method with various payloads
3. Verify status codes and response formats

## 📁 Project Structure

```
9September2025/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── README.md          # This documentation
├── examples/          # Example usage files
│   ├── curl_examples.sh
│   └── python_examples.py
└── tests/             # Test files (optional)
    └── test_api.py
```

## 🏆 Best Practices Demonstrated

1. **RESTful Design:** Proper use of HTTP methods and status codes
2. **Error Handling:** Comprehensive error responses with meaningful messages
3. **Input Validation:** Checking required fields and data types
4. **JSON Responses:** Consistent response format with success/error indicators
5. **HTTP Status Codes:** Appropriate status codes for different scenarios
6. **Idempotency:** Proper implementation of idempotent operations
7. **Resource Identification:** Clear resource identification through URLs
8. **Content Negotiation:** JSON content type handling

## 🔧 Customization

### Adding New Endpoints
1. Define new routes in `app.py`
2. Implement appropriate HTTP methods
3. Add validation and error handling
4. Update this README with new endpoint documentation

### Database Integration
Replace the in-memory storage with a real database:
- SQLite for development
- PostgreSQL/MySQL for production
- Use SQLAlchemy ORM for better database management

### Authentication
Add authentication middleware:
- JWT tokens
- API keys
- OAuth integration

## 🐛 Troubleshooting

### Common Issues

1. **Port already in use:**
   ```bash
   # Kill process using port 5000
   lsof -ti:5000 | xargs kill -9
   ```

2. **Module not found:**
   ```bash
   # Ensure virtual environment is activated
   source flask_env/bin/activate
   pip install -r requirements.txt
   ```

3. **JSON decode error:**
   - Ensure Content-Type header is set to `application/json`
   - Verify JSON syntax in request body

## 📝 Notes

- This is a learning project demonstrating Flask HTTP methods
- In-memory storage means data is lost when server restarts
- For production use, implement proper database integration
- Add authentication and authorization as needed
- Consider implementing rate limiting and logging

## 🤝 Contributing

Feel free to extend this project by:
- Adding DELETE endpoints
- Implementing database integration
- Adding authentication
- Creating comprehensive tests
- Improving error handling

---

**Happy Coding! 🚀**
