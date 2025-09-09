#!/usr/bin/env python3
"""
Simple test script for the Flask API
This script performs basic tests to verify the API is working correctly.
"""

import requests
import json
import sys

def test_api():
    """Test the Flask API endpoints"""
    base_url = "http://localhost:5000"
    
    print("🧪 Testing Flask API...")
    print("=" * 50)
    
    # Test 1: Welcome endpoint
    print("\n1. Testing welcome endpoint...")
    try:
        response = requests.get(f"{base_url}/")
        if response.status_code == 200:
            print("✅ Welcome endpoint working")
        else:
            print(f"❌ Welcome endpoint failed: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to Flask server. Make sure it's running!")
        return False
    
    # Test 2: Get all users
    print("\n2. Testing get all users...")
    try:
        response = requests.get(f"{base_url}/users")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Get all users working - Found {data.get('count', 0)} users")
        else:
            print(f"❌ Get all users failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Get all users error: {e}")
    
    # Test 3: Create user
    print("\n3. Testing create user...")
    try:
        new_user = {
            "name": "Test User",
            "email": "test@example.com",
            "age": 25
        }
        response = requests.post(f"{base_url}/users", json=new_user)
        if response.status_code == 201:
            print("✅ Create user working")
        else:
            print(f"❌ Create user failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Create user error: {e}")
    
    # Test 4: Update user (PATCH)
    print("\n4. Testing update user (PATCH)...")
    try:
        update_data = {"age": 26}
        response = requests.patch(f"{base_url}/users/1", json=update_data)
        if response.status_code == 200:
            print("✅ Update user (PATCH) working")
        else:
            print(f"❌ Update user (PATCH) failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Update user (PATCH) error: {e}")
    
    # Test 5: Update user (PUT)
    print("\n5. Testing update user (PUT)...")
    try:
        update_data = {
            "name": "Updated User",
            "email": "updated@example.com",
            "age": 27
        }
        response = requests.put(f"{base_url}/users/1", json=update_data)
        if response.status_code == 200:
            print("✅ Update user (PUT) working")
        else:
            print(f"❌ Update user (PUT) failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Update user (PUT) error: {e}")
    
    # Test 6: Delete user
    print("\n6. Testing delete user...")
    try:
        response = requests.delete(f"{base_url}/users/2")
        if response.status_code == 200:
            print("✅ Delete user working")
        else:
            print(f"❌ Delete user failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Delete user error: {e}")
    
    # Test 7: HEAD request
    print("\n7. Testing HEAD request...")
    try:
        response = requests.head(f"{base_url}/users")
        if response.status_code == 200:
            print("✅ HEAD request working")
        else:
            print(f"❌ HEAD request failed: {response.status_code}")
    except Exception as e:
        print(f"❌ HEAD request error: {e}")
    
    # Test 8: OPTIONS request
    print("\n8. Testing OPTIONS request...")
    try:
        response = requests.options(f"{base_url}/users")
        if response.status_code == 200:
            print("✅ OPTIONS request working")
        else:
            print(f"❌ OPTIONS request failed: {response.status_code}")
    except Exception as e:
        print(f"❌ OPTIONS request error: {e}")
    
    print("\n" + "=" * 50)
    print("🎉 API testing completed!")
    return True

if __name__ == "__main__":
    success = test_api()
    sys.exit(0 if success else 1)
