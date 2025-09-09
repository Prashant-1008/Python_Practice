from flask import Flask, request, jsonify
from datetime import datetime
import json
import os

# Initialize Flask app
app = Flask(__name__)

# In-memory storage for demonstration (in production, use a database)
users = [
    {"id": 1, "name": "John Doe", "email": "john@example.com", "age": 30, "created_at": "2025-01-01T10:00:00Z"},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com", "age": 25, "created_at": "2025-01-02T11:00:00Z"},
    {"id": 3, "name": "Bob Johnson", "email": "bob@example.com", "age": 35, "created_at": "2025-01-03T12:00:00Z"}
]

next_id = 4

# Helper function to find user by ID
def find_user_by_id(user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None

# Helper function to get next available ID
def get_next_id():
    global next_id
    current_id = next_id
    next_id += 1
    return current_id

# GET Routes
@app.route('/', methods=['GET'])
def home():
    """Welcome endpoint"""
    return jsonify({
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
    })

@app.route('/users', methods=['GET'])
def get_all_users():
    """Get all users"""
    return jsonify({
        "success": True,
        "count": len(users),
        "data": users
    })

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Get a specific user by ID"""
    user = find_user_by_id(user_id)
    if user:
        return jsonify({
            "success": True,
            "data": user
        })
    else:
        return jsonify({
            "success": False,
            "message": f"User with ID {user_id} not found"
        }), 404

# POST Routes
@app.route('/users', methods=['POST'])
def create_user():
    """Create a new user"""
    try:
        data = request.get_json()
        
        # Validate required fields
        if not data:
            return jsonify({
                "success": False,
                "message": "No JSON data provided"
            }), 400
        
        required_fields = ['name', 'email']
        for field in required_fields:
            if field not in data:
                return jsonify({
                    "success": False,
                    "message": f"Missing required field: {field}"
                }), 400
        
        # Check if email already exists
        for user in users:
            if user["email"] == data["email"]:
                return jsonify({
                    "success": False,
                    "message": "Email already exists"
                }), 409
        
        # Create new user
        new_user = {
            "id": get_next_id(),
            "name": data["name"],
            "email": data["email"],
            "age": data.get("age", None),
            "created_at": datetime.now().isoformat() + "Z"
        }
        
        users.append(new_user)
        
        return jsonify({
            "success": True,
            "message": "User created successfully",
            "data": new_user
        }), 201
        
    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Error creating user: {str(e)}"
        }), 500

# PUT Routes (Complete replacement)
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user_put(user_id):
    """Update a user completely (PUT - replace entire resource)"""
    try:
        user = find_user_by_id(user_id)
        if not user:
            return jsonify({
                "success": False,
                "message": f"User with ID {user_id} not found"
            }), 404
        
        data = request.get_json()
        if not data:
            return jsonify({
                "success": False,
                "message": "No JSON data provided"
            }), 400
        
        # Validate required fields for PUT
        required_fields = ['name', 'email']
        for field in required_fields:
            if field not in data:
                return jsonify({
                    "success": False,
                    "message": f"Missing required field: {field}"
                }), 400
        
        # Check if email already exists (excluding current user)
        for existing_user in users:
            if existing_user["email"] == data["email"] and existing_user["id"] != user_id:
                return jsonify({
                    "success": False,
                    "message": "Email already exists"
                }), 409
        
        # Update user completely
        user["name"] = data["name"]
        user["email"] = data["email"]
        user["age"] = data.get("age", None)
        user["updated_at"] = datetime.now().isoformat() + "Z"
        
        return jsonify({
            "success": True,
            "message": "User updated successfully",
            "data": user
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Error updating user: {str(e)}"
        }), 500

# PATCH Routes (Partial update)
@app.route('/users/<int:user_id>', methods=['PATCH'])
def update_user_patch(user_id):
    """Update a user partially (PATCH - update only provided fields)"""
    try:
        user = find_user_by_id(user_id)
        if not user:
            return jsonify({
                "success": False,
                "message": f"User with ID {user_id} not found"
            }), 404
        
        data = request.get_json()
        if not data:
            return jsonify({
                "success": False,
                "message": "No JSON data provided"
            }), 400
        
        # Check if email already exists (excluding current user)
        if "email" in data:
            for existing_user in users:
                if existing_user["email"] == data["email"] and existing_user["id"] != user_id:
                    return jsonify({
                        "success": False,
                        "message": "Email already exists"
                    }), 409
        
        # Update only provided fields
        updated_fields = []
        for field, value in data.items():
            if field in ["name", "email", "age"]:
                user[field] = value
                updated_fields.append(field)
        
        if updated_fields:
            user["updated_at"] = datetime.now().isoformat() + "Z"
            return jsonify({
                "success": True,
                "message": f"User updated successfully. Updated fields: {', '.join(updated_fields)}",
                "data": user
            })
        else:
            return jsonify({
                "success": False,
                "message": "No valid fields to update"
            }), 400
        
    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Error updating user: {str(e)}"
        }), 500

# DELETE Routes
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Delete a user by ID"""
    try:
        user = find_user_by_id(user_id)
        if not user:
            return jsonify({
                "success": False,
                "message": f"User with ID {user_id} not found"
            }), 404
        
        # Remove user from list
        users.remove(user)
        
        return jsonify({
            "success": True,
            "message": f"User with ID {user_id} deleted successfully"
        }), 200
        
    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Error deleting user: {str(e)}"
        }), 500

# HEAD Routes (same as GET but without response body)
@app.route('/users', methods=['HEAD'])
def head_all_users():
    """Get headers for all users endpoint"""
    response = jsonify({
        "success": True,
        "count": len(users),
        "data": users
    })
    # Remove the response body for HEAD request
    response.data = b''
    return response

@app.route('/users/<int:user_id>', methods=['HEAD'])
def head_user(user_id):
    """Get headers for specific user endpoint"""
    user = find_user_by_id(user_id)
    if user:
        response = jsonify({
            "success": True,
            "data": user
        })
    else:
        response = jsonify({
            "success": False,
            "message": f"User with ID {user_id} not found"
        })
        response.status_code = 404
    
    # Remove the response body for HEAD request
    response.data = b''
    return response

# OPTIONS Routes (for CORS and method discovery)
@app.route('/', methods=['OPTIONS'])
def options_home():
    """Handle OPTIONS request for home endpoint"""
    response = jsonify({
        "message": "Available methods for this endpoint",
        "allowed_methods": ["GET", "OPTIONS"]
    })
    response.headers['Allow'] = 'GET, OPTIONS'
    response.headers['Access-Control-Allow-Methods'] = 'GET, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

@app.route('/users', methods=['OPTIONS'])
def options_users():
    """Handle OPTIONS request for users collection endpoint"""
    response = jsonify({
        "message": "Available methods for /users endpoint",
        "allowed_methods": ["GET", "POST", "HEAD", "OPTIONS"],
        "description": {
            "GET": "Retrieve all users",
            "POST": "Create a new user",
            "HEAD": "Get headers only (no body)",
            "OPTIONS": "Get allowed methods"
        }
    })
    response.headers['Allow'] = 'GET, POST, HEAD, OPTIONS'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, HEAD, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

@app.route('/users/<int:user_id>', methods=['OPTIONS'])
def options_user(user_id):
    """Handle OPTIONS request for specific user endpoint"""
    response = jsonify({
        "message": f"Available methods for /users/{user_id} endpoint",
        "allowed_methods": ["GET", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS"],
        "description": {
            "GET": "Retrieve user by ID",
            "PUT": "Update user completely",
            "PATCH": "Update user partially",
            "DELETE": "Delete user",
            "HEAD": "Get headers only (no body)",
            "OPTIONS": "Get allowed methods"
        }
    })
    response.headers['Allow'] = 'GET, PUT, PATCH, DELETE, HEAD, OPTIONS'
    response.headers['Access-Control-Allow-Methods'] = 'GET, PUT, PATCH, DELETE, HEAD, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "message": "Endpoint not found"
    }), 404

@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({
        "success": False,
        "message": "Method not allowed for this endpoint"
    }), 405

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        "success": False,
        "message": "Internal server error"
    }), 500

if __name__ == '__main__':
    print("Starting Flask API Practice Server...")
    print("Available endpoints:")
    print("  GET     /           - Welcome message")
    print("  GET     /users      - Get all users")
    print("  GET     /users/<id> - Get specific user")
    print("  POST    /users      - Create new user")
    print("  PUT     /users/<id> - Update user completely")
    print("  PATCH   /users/<id> - Update user partially")
    print("  DELETE  /users/<id> - Delete user")
    print("  HEAD    /users      - Get headers for all users")
    print("  HEAD    /users/<id> - Get headers for specific user")
    print("  OPTIONS /           - Get allowed methods for home")
    print("  OPTIONS /users      - Get allowed methods for users")
    print("  OPTIONS /users/<id> - Get allowed methods for specific user")
    print("\nServer will start on http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
