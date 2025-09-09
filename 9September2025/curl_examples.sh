#!/bin/bash

# Flask API Practice - curl Examples
# Make sure the Flask server is running on http://localhost:5000

BASE_URL="http://localhost:5000"

echo "=== Flask API Practice - curl Examples ==="
echo "Base URL: $BASE_URL"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print section headers
print_section() {
    echo -e "${BLUE}=== $1 ===${NC}"
    echo ""
}

# Function to print command
print_command() {
    echo -e "${YELLOW}Command:${NC} $1"
    echo ""
}

# Function to print response
print_response() {
    echo -e "${GREEN}Response:${NC}"
    echo "$1"
    echo ""
    echo "----------------------------------------"
    echo ""
}

print_section "1. GET - Welcome Endpoint"
print_command "curl -X GET $BASE_URL/"
response=$(curl -s -X GET "$BASE_URL/")
print_response "$response"

print_section "2. GET - All Users"
print_command "curl -X GET $BASE_URL/users"
response=$(curl -s -X GET "$BASE_URL/users")
print_response "$response"

print_section "3. GET - Specific User (ID: 1)"
print_command "curl -X GET $BASE_URL/users/1"
response=$(curl -s -X GET "$BASE_URL/users/1")
print_response "$response"

print_section "4. GET - Non-existent User (ID: 999)"
print_command "curl -X GET $BASE_URL/users/999"
response=$(curl -s -X GET "$BASE_URL/users/999")
print_response "$response"

print_section "5. POST - Create New User"
print_command "curl -X POST $BASE_URL/users -H 'Content-Type: application/json' -d '{\"name\": \"Alice Johnson\", \"email\": \"alice@example.com\", \"age\": 28}'"
response=$(curl -s -X POST "$BASE_URL/users" \
    -H "Content-Type: application/json" \
    -d '{"name": "Alice Johnson", "email": "alice@example.com", "age": 28}')
print_response "$response"

print_section "6. POST - Create User with Missing Required Field"
print_command "curl -X POST $BASE_URL/users -H 'Content-Type: application/json' -d '{\"name\": \"Bob Smith\"}'"
response=$(curl -s -X POST "$BASE_URL/users" \
    -H "Content-Type: application/json" \
    -d '{"name": "Bob Smith"}')
print_response "$response"

print_section "7. POST - Create User with Duplicate Email"
print_command "curl -X POST $BASE_URL/users -H 'Content-Type: application/json' -d '{\"name\": \"John Duplicate\", \"email\": \"john@example.com\"}'"
response=$(curl -s -X POST "$BASE_URL/users" \
    -H "Content-Type: application/json" \
    -d '{"name": "John Duplicate", "email": "john@example.com"}')
print_response "$response"

print_section "8. PUT - Complete User Update (ID: 1)"
print_command "curl -X PUT $BASE_URL/users/1 -H 'Content-Type: application/json' -d '{\"name\": \"John Updated\", \"email\": \"john.updated@example.com\", \"age\": 31}'"
response=$(curl -s -X PUT "$BASE_URL/users/1" \
    -H "Content-Type: application/json" \
    -d '{"name": "John Updated", "email": "john.updated@example.com", "age": 31}')
print_response "$response"

print_section "9. PUT - Update Non-existent User"
print_command "curl -X PUT $BASE_URL/users/999 -H 'Content-Type: application/json' -d '{\"name\": \"Non Existent\", \"email\": \"nonexistent@example.com\"}'"
response=$(curl -s -X PUT "$BASE_URL/users/999" \
    -H "Content-Type: application/json" \
    -d '{"name": "Non Existent", "email": "nonexistent@example.com"}')
print_response "$response"

print_section "10. PATCH - Partial User Update (ID: 1)"
print_command "curl -X PATCH $BASE_URL/users/1 -H 'Content-Type: application/json' -d '{\"age\": 32}'"
response=$(curl -s -X PATCH "$BASE_URL/users/1" \
    -H "Content-Type: application/json" \
    -d '{"age": 32}')
print_response "$response"

print_section "11. PATCH - Update Multiple Fields (ID: 2)"
print_command "curl -X PATCH $BASE_URL/users/2 -H 'Content-Type: application/json' -d '{\"name\": \"Jane Updated\", \"age\": 26}'"
response=$(curl -s -X PATCH "$BASE_URL/users/2" \
    -H "Content-Type: application/json" \
    -d '{"name": "Jane Updated", "age": 26}')
print_response "$response"

print_section "12. PATCH - Update Non-existent User"
print_command "curl -X PATCH $BASE_URL/users/999 -H 'Content-Type: application/json' -d '{\"age\": 25}'"
response=$(curl -s -X PATCH "$BASE_URL/users/999" \
    -H "Content-Type: application/json" \
    -d '{"age": 25}')
print_response "$response"

print_section "13. DELETE - Delete User (ID: 3)"
print_command "curl -X DELETE $BASE_URL/users/3"
response=$(curl -s -X DELETE "$BASE_URL/users/3")
print_response "$response"

print_section "14. DELETE - Delete Non-existent User"
print_command "curl -X DELETE $BASE_URL/users/999"
response=$(curl -s -X DELETE "$BASE_URL/users/999")
print_response "$response"

print_section "15. HEAD - Get Headers for All Users"
print_command "curl -I $BASE_URL/users"
response=$(curl -s -I "$BASE_URL/users")
print_response "$response"

print_section "16. HEAD - Get Headers for Specific User (ID: 1)"
print_command "curl -I $BASE_URL/users/1"
response=$(curl -s -I "$BASE_URL/users/1")
print_response "$response"

print_section "17. HEAD - Get Headers for Non-existent User"
print_command "curl -I $BASE_URL/users/999"
response=$(curl -s -I "$BASE_URL/users/999")
print_response "$response"

print_section "18. OPTIONS - Get Allowed Methods for Home"
print_command "curl -X OPTIONS $BASE_URL/"
response=$(curl -s -X OPTIONS "$BASE_URL/")
print_response "$response"

print_section "19. OPTIONS - Get Allowed Methods for Users"
print_command "curl -X OPTIONS $BASE_URL/users"
response=$(curl -s -X OPTIONS "$BASE_URL/users")
print_response "$response"

print_section "20. OPTIONS - Get Allowed Methods for Specific User"
print_command "curl -X OPTIONS $BASE_URL/users/1"
response=$(curl -s -X OPTIONS "$BASE_URL/users/1")
print_response "$response"

print_section "21. GET - Verify Final State (All Users)"
print_command "curl -X GET $BASE_URL/users"
response=$(curl -s -X GET "$BASE_URL/users")
print_response "$response"

echo -e "${GREEN}=== All Examples Completed ===${NC}"
echo ""
echo "Tips:"
echo "- Make sure Flask server is running: python app.py"
echo "- Check server logs for detailed request/response information"
echo "- Modify the examples to test different scenarios"
echo "- Use tools like Postman for more advanced testing"
