"""
Data models for the Flask API Practice
This file contains data structures and validation logic for the user management system.
"""

from datetime import datetime
from typing import Dict, Any, List, Optional
import re

class User:
    """User model class"""
    
    def __init__(self, user_id: int, name: str, email: str, age: Optional[int] = None):
        self.id = user_id
        self.name = name
        self.email = email
        self.age = age
        self.created_at = datetime.now().isoformat() + "Z"
        self.updated_at = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert user object to dictionary"""
        user_dict = {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "age": self.age,
            "created_at": self.created_at
        }
        if self.updated_at:
            user_dict["updated_at"] = self.updated_at
        return user_dict
    
    def update(self, **kwargs) -> List[str]:
        """Update user fields and return list of updated fields"""
        updated_fields = []
        
        if "name" in kwargs:
            self.name = kwargs["name"]
            updated_fields.append("name")
        
        if "email" in kwargs:
            self.email = kwargs["email"]
            updated_fields.append("email")
        
        if "age" in kwargs:
            self.age = kwargs["age"]
            updated_fields.append("age")
        
        if updated_fields:
            self.updated_at = datetime.now().isoformat() + "Z"
        
        return updated_fields
    
    @staticmethod
    def validate_email(email: str) -> bool:
        """Validate email format"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    @staticmethod
    def validate_name(name: str) -> bool:
        """Validate name format"""
        return len(name.strip()) >= 2 and name.replace(" ", "").isalpha()
    
    @staticmethod
    def validate_age(age: Any) -> bool:
        """Validate age format"""
        if age is None:
            return True
        return isinstance(age, int) and 0 <= age <= 150

class UserValidator:
    """Validation class for user data"""
    
    @staticmethod
    def validate_user_data(data: Dict[str, Any], required_fields: List[str] = None) -> Dict[str, Any]:
        """
        Validate user data and return validation result
        
        Args:
            data: User data dictionary
            required_fields: List of required fields (default: ['name', 'email'])
        
        Returns:
            Dictionary with 'valid' boolean and 'errors' list
        """
        if required_fields is None:
            required_fields = ['name', 'email']
        
        errors = []
        
        # Check required fields
        for field in required_fields:
            if field not in data or not data[field]:
                errors.append(f"Missing required field: {field}")
        
        # Validate name
        if 'name' in data and data['name']:
            if not User.validate_name(data['name']):
                errors.append("Name must be at least 2 characters and contain only letters and spaces")
        
        # Validate email
        if 'email' in data and data['email']:
            if not User.validate_email(data['email']):
                errors.append("Invalid email format")
        
        # Validate age
        if 'age' in data:
            if not User.validate_age(data['age']):
                errors.append("Age must be a number between 0 and 150")
        
        return {
            'valid': len(errors) == 0,
            'errors': errors
        }

class UserManager:
    """User management class for in-memory storage"""
    
    def __init__(self):
        self.users: List[User] = []
        self.next_id = 1
        self._initialize_sample_data()
    
    def _initialize_sample_data(self):
        """Initialize with sample data"""
        sample_users = [
            {"name": "John Doe", "email": "john@example.com", "age": 30},
            {"name": "Jane Smith", "email": "jane@example.com", "age": 25},
            {"name": "Bob Johnson", "email": "bob@example.com", "age": 35}
        ]
        
        for user_data in sample_users:
            user = User(self.next_id, **user_data)
            self.users.append(user)
            self.next_id += 1
    
    def get_all_users(self) -> List[Dict[str, Any]]:
        """Get all users as dictionaries"""
        return [user.to_dict() for user in self.users]
    
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        """Get user by ID"""
        for user in self.users:
            if user.id == user_id:
                return user
        return None
    
    def get_user_by_email(self, email: str) -> Optional[User]:
        """Get user by email"""
        for user in self.users:
            if user.email == email:
                return user
        return None
    
    def create_user(self, user_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create new user"""
        # Validate data
        validation = UserValidator.validate_user_data(user_data)
        if not validation['valid']:
            return {
                'success': False,
                'message': '; '.join(validation['errors'])
            }
        
        # Check if email already exists
        if self.get_user_by_email(user_data['email']):
            return {
                'success': False,
                'message': 'Email already exists'
            }
        
        # Create user
        user = User(self.next_id, **user_data)
        self.users.append(user)
        self.next_id += 1
        
        return {
            'success': True,
            'message': 'User created successfully',
            'data': user.to_dict()
        }
    
    def update_user_put(self, user_id: int, user_data: Dict[str, Any]) -> Dict[str, Any]:
        """Update user completely (PUT)"""
        user = self.get_user_by_id(user_id)
        if not user:
            return {
                'success': False,
                'message': f'User with ID {user_id} not found'
            }
        
        # Validate data
        validation = UserValidator.validate_user_data(user_data)
        if not validation['valid']:
            return {
                'success': False,
                'message': '; '.join(validation['errors'])
            }
        
        # Check if email already exists (excluding current user)
        existing_user = self.get_user_by_email(user_data['email'])
        if existing_user and existing_user.id != user_id:
            return {
                'success': False,
                'message': 'Email already exists'
            }
        
        # Update user
        user.name = user_data['name']
        user.email = user_data['email']
        user.age = user_data.get('age')
        user.updated_at = datetime.now().isoformat() + "Z"
        
        return {
            'success': True,
            'message': 'User updated successfully',
            'data': user.to_dict()
        }
    
    def update_user_patch(self, user_id: int, user_data: Dict[str, Any]) -> Dict[str, Any]:
        """Update user partially (PATCH)"""
        user = self.get_user_by_id(user_id)
        if not user:
            return {
                'success': False,
                'message': f'User with ID {user_id} not found'
            }
        
        # Validate only provided fields
        validation = UserValidator.validate_user_data(user_data, [])
        if not validation['valid']:
            return {
                'success': False,
                'message': '; '.join(validation['errors'])
            }
        
        # Check if email already exists (excluding current user)
        if 'email' in user_data:
            existing_user = self.get_user_by_email(user_data['email'])
            if existing_user and existing_user.id != user_id:
                return {
                    'success': False,
                    'message': 'Email already exists'
                }
        
        # Update only provided fields
        updated_fields = user.update(**user_data)
        
        if updated_fields:
            return {
                'success': True,
                'message': f'User updated successfully. Updated fields: {", ".join(updated_fields)}',
                'data': user.to_dict()
            }
        else:
            return {
                'success': False,
                'message': 'No valid fields to update'
            }
    
    def delete_user(self, user_id: int) -> Dict[str, Any]:
        """Delete user by ID"""
        user = self.get_user_by_id(user_id)
        if not user:
            return {
                'success': False,
                'message': f'User with ID {user_id} not found'
            }
        
        self.users.remove(user)
        return {
            'success': True,
            'message': 'User deleted successfully'
        }
    
    def get_user_count(self) -> int:
        """Get total number of users"""
        return len(self.users)

# Sample data for demonstration
SAMPLE_USERS = [
    {"id": 1, "name": "John Doe", "email": "john@example.com", "age": 30, "created_at": "2025-01-01T10:00:00Z"},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com", "age": 25, "created_at": "2025-01-02T11:00:00Z"},
    {"id": 3, "name": "Bob Johnson", "email": "bob@example.com", "age": 35, "created_at": "2025-01-03T12:00:00Z"}
]

# Example usage
if __name__ == "__main__":
    # Create user manager
    manager = UserManager()
    
    # Display all users
    print("All users:")
    for user in manager.get_all_users():
        print(f"  {user}")
    
    # Create new user
    print("\nCreating new user...")
    result = manager.create_user({
        "name": "Alice Johnson",
        "email": "alice@example.com",
        "age": 28
    })
    print(f"Result: {result}")
    
    # Update user partially
    print("\nUpdating user partially...")
    result = manager.update_user_patch(1, {"age": 31})
    print(f"Result: {result}")
    
    # Update user completely
    print("\nUpdating user completely...")
    result = manager.update_user_put(2, {
        "name": "Jane Updated",
        "email": "jane.updated@example.com",
        "age": 26
    })
    print(f"Result: {result}")
    
    # Display final state
    print("\nFinal users:")
    for user in manager.get_all_users():
        print(f"  {user}")
