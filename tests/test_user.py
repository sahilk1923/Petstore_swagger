import copy
import pytest
from utils.api_client import ApiClient
from utils.config import BASE_URL, HEADERS, HEADERS1

from data.user_data import get_user_data

client = ApiClient(BASE_URL)


@pytest.fixture
def create_user():
    user_data=get_user_data()
    response = client.post("/user", user_data, HEADERS)
    return response

@pytest.mark.create_user  # Add marker here
def test_create_user():
    user_data=get_user_data()
    response = client.post("/user", user_data, HEADERS)
    if response is None:
        pytest.fail("Request failed; cannot proceed with further checks.")

    print("create user response:",response)

    # Assertions
    # Validate the response content
    validate_create_user_resposne(response)
    
@pytest.mark.skip  # Skip this test for now
def validate_create_user_resposne(response):
    assert response.status_code in [200, 201], f"Unexpected status code: {response.status_code}"

    # Check the response body format
    try:
        response_json = response.json()  # Attempt to parse the JSON response
    except ValueError:
        pytest.fail("Response content is not valid JSON.")
    
    assert isinstance(response_json, dict), "Response is not a JSON object." 
    assert len(response_json["message"]) > 0  # Ensure the message is not empty
    assert "code" in response_json,"'code' is missing from the response."
    assert "type" in response_json, "'type' is missing from the response." # Check if 'type' is in the response
    assert "message" in response_json,  "'message' is missing from the response."
    assert response_json["code"] == 200, "Expected 'code' to be 200."  # Check if the 'code' is 200
    assert response_json["type"] == "unknown", "Expected 'type' to be 'unknown'."
    user_id = response_json["message"]  # Extracting the ID
    assert isinstance(user_id, str),"Extracted ID is not a string."  # Check if the extracted ID is a string

@pytest.mark.skip  # Skip this test for now
def test_create_duplicate_user():

    user_data = get_user_data()  # Reuse the same user data for duplicate check
    user_data_copy = copy.deepcopy(user_data) 
    user_data_copy['username'] = 'duplicateuser'
    print(user_data_copy)
    # First request: already created user from fixture
    first_response=client.post("/user",user_data_copy,HEADERS)
    
    if first_response is None:
        pytest.fail("Request failed for the first user creation; cannot proceed with further checks.")

    assert first_response.status_code == 200 or first_response.status_code == 201

    # Second request: attempting to create the same user again (duplicate)
    second_response = client.post("/user", user_data_copy,HEADERS)
    if second_response is None:
        pytest.fail("Request failed for the duplicate user creation; cannot proceed with further checks.")
    # Assert that the second creation should fail (duplicate not allowed)
    assert second_response.status_code == 200 or second_response.status_code == 201
    assert "error" in second_response.json()["message"]



@pytest.mark.skip  # Skip this test for now
def test_login_user():
    response = client.get("/user/login?username=testuser&password=password123",HEADERS)
    print(response)
    if response is None:
        pytest.fail("Request failed; cannot proceed with further checks.")
    assert response.status_code == 200

def test_get_user_by_username():
    user_data = get_user_data()  # Reuse the same user data for duplicate check
    user_data_copy = copy.deepcopy(user_data) 
    response = client.get(f"/user/{user_data_copy['username']}",HEADERS)
    if response is None:
        pytest.fail("Request failed; cannot proceed with further checks.")
    print(response)
    assert response.status_code == 200
    assert response.json()["username"] == "test_user"

def test_delete_user_by_username():
    user_data = get_user_data()  # Reuse the same user data for duplicate check
    user_data_copy = copy.deepcopy(user_data) 
    
    response = client.delete(f"/user/{user_data_copy['username']}",HEADERS)
    if response is None:
        pytest.fail("Request failed; cannot proceed with further checks.")
    print(response)
    assert response.status_code == 200


# create user

# This can only be done by the logged in user.
# Request body
# {
#   "id": 0,
#   "username": "string",
#   "firstName": "string",
#   "lastName": "string",
#   "email": "string",
#   "password": "string",
#   "phone": "string",
#   "userStatus": 0
# }
# Response content type xml and json
#curl
# curl -X 'POST' \
#   'https://petstore.swagger.io/v2/user' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d '{
#   "id": 0,
#   "username": "string",
#   "firstName": "string",
#   "lastName": "string",
#   "email": "string",
#   "password": "string",
#   "phone": "string",
#   "userStatus": 0
# }'
# request url https://petstore.swagger.io/v2/user
# Response body
# {
#   "code": 200,
#   "type": "unknown",
#   "message": "9223372036854761800"
# }

#---------------------------------------------------------------------
# get user by username

# Response content type xml and json
# curl
# curl -X 'GET' \
#   'https://petstore.swagger.io/v2/user/abc' \
#   -H 'accept: application/json'

# Request url https://petstore.swagger.io/v2/user/abc

# Reponse body:
# {
#   "id": 1,
#   "username": "abc",
#   "firstName": "string",
#   "lastName": "string",
#   "email": "string",
#   "password": "string",
#   "phone": "string",
#   "userStatus": 0
# }

#---------------------------------------------------------------------
# update user 

# This can only be done by the logged in user.
# {
#   "id": 0,
#   "username": "string",
#   "firstName": "string",
#   "lastName": "string",
#   "email": "string",
#   "password": "string",
#   "phone": "string",
#   "userStatus": 0
# }
# Response content type xml and json
# Curl

# curl -X 'PUT' \
#   'https://petstore.swagger.io/v2/user/av' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d '{
#   "id": 0,
#   "username": "string",
#   "firstName": "string",
#   "lastName": "string",
#   "email": "string",
#   "password": "string",
#   "phone": "string",
#   "userStatus": 0
# }'
# Request URL
# https://petstore.swagger.io/v2/user/av
# Response body
# {
#   "code": 200,
#   "type": "unknown",
#   "message": "9223372036854761960"
# }

#---------------------------------------------------------------------
# delete user

# Response content type xml and json
# curl -X 'DELETE' \
#   'https://petstore.swagger.io/v2/user/abc' \
#   -H 'accept: application/json'
# Request URL
# https://petstore.swagger.io/v2/user/abc
	
# Response body

# {
#   "code": 200,
#   "type": "unknown",
#   "message": "abc"
# }
#---------------------------------------------------------------------
# user login

# Curl
# curl -X 'GET' \
#   'https://petstore.swagger.io/v2/user/login?username=ab&password=ab' \
#   -H 'accept: application/json'

# Request URL
# https://petstore.swagger.io/v2/user/login?username=ab&password=ab	
# Response body
# {
#   "code": 200,
#   "type": "unknown",
#   "message": "logged in user session:1729685600141"
# }
#---------------------------------------------------------------------

# user logout.
# Curl

# curl -X 'GET' \
#   'https://petstore.swagger.io/v2/user/logout' \
#   -H 'accept: application/json'


# https://petstore.swagger.io/v2/user/logout


# {
#   "code": 200,
#   "type": "unknown",
#   "message": "ok"
# }