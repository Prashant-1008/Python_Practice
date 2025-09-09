#!/usr/bin/env python3
"""
Flask API Practice - Python Examples
This script demonstrates how to interact with the Flask API using Python requests library.

Make sure to:
1. Install requests: pip install requests
2. Start the Flask server: python app.py
3. Run this script: python python_examples.py
"""

import requests
import json
import time
from typing import Dict, Any, Optional

class FlaskAPIClient:
    """Client class for interacting with the Flask API"""
    
    def __init__(self, base_url: str = "http://localhost:5000"):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
    
    def get_welcome(self) -> Dict[str, Any]:
        """Get welcome message"""
        response = self.session.get(f"{self.base_url}/")
        return self._handle_response(response)
    
    def get_all_users(self) -> Dict[str, Any]:
        """Get all users"""
        response = self.session.get(f"{self.base_url}/users")
        return self._handle_response(response)
    
    def get_user(self, user_id: int) -> Dict[str, Any]:
        """Get specific user by ID"""
        response = self.session.get(f"{self.base_url}/users/{user_id}")
        return self._handle_response(response)
    
    def create_user(self, user_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create new user"""
        response = self.session.post(f"{self.base_url}/users", json=user_data)
        return self._handle_response(response)
    
    def update_user_put(self, user_id: int, user_data: Dict[str, Any]) -> Dict[str, Any]:
        """Update user completely (PUT)"""
        response = self.session.put(f"{self.base_url}/users/{user_id}", json=user_data)
        return self._handle_response(response)
    
    def update_user_patch(self, user_id: int, user_data: Dict[str, Any]) -> Dict[str, Any]:
        """Update user partially (PATCH)"""
        response = self.session.patch(f"{self.base_url}/users/{user_id}", json=user_data)
        return self._handle_response(response)
    
    def delete_user(self, user_id: int) -> Dict[str, Any]:
        """Delete user by ID"""
        response = self.session.delete(f"{self.base_url}/users/{user_id}")
        return self._handle_response(response)
    
    def head_all_users(self) -> Dict[str, Any]:
        """Get headers for all users (HEAD)"""
        response = self.session.head(f"{self.base_url}/users")
        return self._handle_response(response)
    
    def head_user(self, user_id: int) -> Dict[str, Any]:
        """Get headers for specific user (HEAD)"""
        response = self.session.head(f"{self.base_url}/users/{user_id}")
        return self._handle_response(response)
    
    def options_home(self) -> Dict[str, Any]:
        """Get allowed methods for home endpoint (OPTIONS)"""
        response = self.session.options(f"{self.base_url}/")
        return self._handle_response(response)
    
    def options_users(self) -> Dict[str, Any]:
        """Get allowed methods for users endpoint (OPTIONS)"""
        response = self.session.options(f"{self.base_url}/users")
        return self._handle_response(response)
    
    def options_user(self, user_id: int) -> Dict[str, Any]:
        """Get allowed methods for specific user endpoint (OPTIONS)"""
        response = self.session.options(f"{self.base_url}/users/{user_id}")
        return self._handle_response(response)
    
    def _handle_response(self, response: requests.Response) -> Dict[str, Any]:
        """Handle API response and return formatted result"""
        try:
            data = response.json()
            return {
                'status_code': response.status_code,
                'success': response.status_code < 400,
                'data': data,
                'headers': dict(response.headers)
            }
        except json.JSONDecodeError:
            return {
                'status_code': response.status_code,
                'success': False,
                'data': {'error': 'Invalid JSON response'},
                'headers': dict(response.headers)
            }

def print_section(title: str):
    """Print section header"""
    print(f"\n{'='*60}")
    print(f" {title}")
    print(f"{'='*60}")

def print_result(operation: str, result: Dict[str, Any]):
    """Print operation result"""
    print(f"\n{operation}:")
    print(f"Status Code: {result['status_code']}")
    print(f"Success: {result['success']}")
    print(f"Response:")
    print(json.dumps(result['data'], indent=2))

def main():
    """Main function demonstrating API usage"""
    print("Flask API Practice - Python Examples")
    print("Make sure the Flask server is running on http://localhost:5000")
    
    # Initialize API client
    api = FlaskAPIClient()
    
    try:
        # Test 1: Welcome endpoint
        print_section("1. GET - Welcome Endpoint")
        result = api.get_welcome()
        print_result("Welcome Message", result)
        
        # Test 2: Get all users
        print_section("2. GET - All Users")
        result = api.get_all_users()
        print_result("All Users", result)
        
        # Test 3: Get specific user
        print_section("3. GET - Specific User (ID: 1)")
        result = api.get_user(1)
        print_result("User ID 1", result)
        
        # Test 4: Get non-existent user
        print_section("4. GET - Non-existent User (ID: 999)")
        result = api.get_user(999)
        print_result("User ID 999", result)
        
        # Test 5: Create new user
        print_section("5. POST - Create New User")
        new_user = {
            "name": "Alice Johnson",
            "email": "alice@example.com",
            "age": 28
        }
        result = api.create_user(new_user)
        print_result("Create User", result)
        
        # Store the new user ID for further tests
        new_user_id = None
        if result['success'] and 'data' in result['data'] and 'id' in result['data']['data']:
            new_user_id = result['data']['data']['id']
        
        # Test 6: Create user with missing required field
        print_section("6. POST - Create User with Missing Required Field")
        incomplete_user = {
            "name": "Bob Smith"
            # Missing email field
        }
        result = api.create_user(incomplete_user)
        print_result("Create Incomplete User", result)
        
        # Test 7: Create user with duplicate email
        print_section("7. POST - Create User with Duplicate Email")
        duplicate_user = {
            "name": "John Duplicate",
            "email": "john@example.com"  # This email already exists
        }
        result = api.create_user(duplicate_user)
        print_result("Create Duplicate User", result)
        
        # Test 8: Update user completely (PUT)
        print_section("8. PUT - Complete User Update (ID: 1)")
        update_data = {
            "name": "John Updated",
            "email": "john.updated@example.com",
            "age": 31
        }
        result = api.update_user_put(1, update_data)
        print_result("Update User (PUT)", result)
        
        # Test 9: Update non-existent user
        print_section("9. PUT - Update Non-existent User")
        result = api.update_user_put(999, update_data)
        print_result("Update Non-existent User", result)
        
        # Test 10: Update user partially (PATCH)
        print_section("10. PATCH - Partial User Update (ID: 1)")
        partial_update = {
            "age": 32
        }
        result = api.update_user_patch(1, partial_update)
        print_result("Update User (PATCH)", result)
        
        # Test 11: Update multiple fields (PATCH)
        print_section("11. PATCH - Update Multiple Fields (ID: 2)")
        multi_update = {
            "name": "Jane Updated",
            "age": 26
        }
        result = api.update_user_patch(2, multi_update)
        print_result("Update Multiple Fields", result)
        
        # Test 12: Update non-existent user (PATCH)
        print_section("12. PATCH - Update Non-existent User")
        result = api.update_user_patch(999, partial_update)
        print_result("Update Non-existent User (PATCH)", result)
        
        # Test 13: Delete user
        print_section("13. DELETE - Delete User (ID: 3)")
        result = api.delete_user(3)
        print_result("Delete User", result)
        
        # Test 14: Delete non-existent user
        print_section("14. DELETE - Delete Non-existent User")
        result = api.delete_user(999)
        print_result("Delete Non-existent User", result)
        
        # Test 15: HEAD - Get headers for all users
        print_section("15. HEAD - Get Headers for All Users")
        result = api.head_all_users()
        print_result("HEAD All Users", result)
        
        # Test 16: HEAD - Get headers for specific user
        print_section("16. HEAD - Get Headers for Specific User (ID: 1)")
        result = api.head_user(1)
        print_result("HEAD User", result)
        
        # Test 17: HEAD - Get headers for non-existent user
        print_section("17. HEAD - Get Headers for Non-existent User")
        result = api.head_user(999)
        print_result("HEAD Non-existent User", result)
        
        # Test 18: OPTIONS - Get allowed methods for home
        print_section("18. OPTIONS - Get Allowed Methods for Home")
        result = api.options_home()
        print_result("OPTIONS Home", result)
        
        # Test 19: OPTIONS - Get allowed methods for users
        print_section("19. OPTIONS - Get Allowed Methods for Users")
        result = api.options_users()
        print_result("OPTIONS Users", result)
        
        # Test 20: OPTIONS - Get allowed methods for specific user
        print_section("20. OPTIONS - Get Allowed Methods for Specific User")
        result = api.options_user(1)
        print_result("OPTIONS User", result)
        
        # Test 21: Verify final state
        print_section("21. GET - Verify Final State")
        result = api.get_all_users()
        print_result("All Users (Final State)", result)
        
        # Test 22: Demonstrate error handling
        print_section("22. Error Handling Examples")
        
        # Test with invalid JSON
        print("\nTesting with invalid JSON:")
        try:
            response = requests.post(
                f"{api.base_url}/users",
                data="invalid json",
                headers={'Content-Type': 'application/json'}
            )
            print(f"Status Code: {response.status_code}")
            print(f"Response: {response.text}")
        except Exception as e:
            print(f"Error: {e}")
        
        # Test with wrong content type
        print("\nTesting with wrong content type:")
        try:
            response = requests.post(
                f"{api.base_url}/users",
                data="name=Test&email=test@example.com",
                headers={'Content-Type': 'application/x-www-form-urlencoded'}
            )
            print(f"Status Code: {response.status_code}")
            print(f"Response: {response.text}")
        except Exception as e:
            print(f"Error: {e}")
        
    except requests.exceptions.ConnectionError:
        print("\n❌ Error: Could not connect to Flask server.")
        print("Make sure the server is running: python app.py")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
    
    print_section("Examples Completed")
    print("✅ All API examples have been demonstrated!")
    print("\nTips:")
    print("- Check the Flask server logs for detailed request/response information")
    print("- Modify the examples to test different scenarios")
    print("- Use the FlaskAPIClient class in your own projects")

def demonstrate_advanced_usage():
    """Demonstrate advanced API usage patterns"""
    print_section("Advanced Usage Examples")
    
    api = FlaskAPIClient()
    
    # Batch operations
    print("\n1. Batch User Creation:")
    users_to_create = [
        {"name": "User 1", "email": "user1@example.com", "age": 25},
        {"name": "User 2", "email": "user2@example.com", "age": 30},
        {"name": "User 3", "email": "user3@example.com", "age": 35}
    ]
    
    created_users = []
    for user_data in users_to_create:
        result = api.create_user(user_data)
        if result['success']:
            created_users.append(result['data']['data'])
            print(f"✅ Created: {user_data['name']}")
        else:
            print(f"❌ Failed to create: {user_data['name']} - {result['data'].get('message', 'Unknown error')}")
    
    # Bulk updates
    print(f"\n2. Bulk Updates:")
    for i, user in enumerate(created_users, 1):
        update_data = {"age": user.get('age', 0) + 1}
        result = api.update_user_patch(user['id'], update_data)
        if result['success']:
            print(f"✅ Updated user {user['id']}: age = {update_data['age']}")
        else:
            print(f"❌ Failed to update user {user['id']}")

if __name__ == "__main__":
    main()
    
    # Uncomment the line below to run advanced examples
    # demonstrate_advanced_usage()
