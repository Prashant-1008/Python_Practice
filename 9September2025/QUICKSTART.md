# Quick Start Guide - Flask API Practice (All HTTP Methods)

## 🚀 Get Started in 3 Steps

### 1. Install Dependencies
```bash
cd 9September2025
pip install -r requirements.txt
```

### 2. Start the Server
```bash
python app.py
```

### 3. Test the API
```bash
# Quick test
python test_api.py

# Or run examples
python python_examples.py

# Or use curl examples
./curl_examples.sh
```

## 📋 Available Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message |
| GET | `/users` | Get all users |
| GET | `/users/<id>` | Get specific user |
| POST | `/users` | Create new user |
| PUT | `/users/<id>` | Update user completely |
| PATCH | `/users/<id>` | Update user partially |
| DELETE | `/users/<id>` | Delete user |
| HEAD | `/users` | Get headers for all users |
| HEAD | `/users/<id>` | Get headers for specific user |
| OPTIONS | `/` | Get allowed methods for home |
| OPTIONS | `/users` | Get allowed methods for users |
| OPTIONS | `/users/<id>` | Get allowed methods for specific user |

## 🧪 Quick Test Commands

```bash
# Get all users
curl http://localhost:5000/users

# Create a user
curl -X POST http://localhost:5000/users \
  -H "Content-Type: application/json" \
  -d '{"name": "Test User", "email": "test@example.com", "age": 25}'

# Update user (PATCH)
curl -X PATCH http://localhost:5000/users/1 \
  -H "Content-Type: application/json" \
  -d '{"age": 26}'

# Delete user
curl -X DELETE http://localhost:5000/users/1

# Get headers only (HEAD)
curl -I http://localhost:5000/users

# Get allowed methods (OPTIONS)
curl -X OPTIONS http://localhost:5000/users
```

## 📁 Project Files

- `app.py` - Main Flask application
- `models.py` - Data models and validation
- `requirements.txt` - Python dependencies
- `README.md` - Complete documentation
- `test_api.py` - Simple API tests
- `python_examples.py` - Python usage examples
- `curl_examples.sh` - Shell script examples

## 🎯 What You'll Learn

- ✅ Flask route handling
- ✅ All major HTTP methods (GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS)
- ✅ JSON request/response handling
- ✅ Error handling and validation
- ✅ RESTful API design
- ✅ Status codes and best practices
- ✅ CORS and API discovery
- ✅ Resource metadata handling

Happy coding! 🚀
