# Testing Overview

## Tested Endpoints:
**User**: Create User, Get user by user name, Update user by user name, delete user by user name, user login and user logout
***Note: Tested using JSON format ***
**Pet**: Adding a new pet to the store, find pet by ID, updating an existing pet and delete pet by petID
***Note: Tested using XML format***


## Key Focus Areas:
- API key authentication
- OAuth2 authentication
- User session validation
- Status code validation (e.g., 200, 400, 404, 500)
- Response body validation
- Invalid inputs, incorrect formats, and edge case scenarios

## Potential Areas for Additional Testing:
- Test the remaining endpoints for functionality
- Testing with null or empty values in the request body
- Specifying different content types (e.g., application/json, application/xml)
- Testing with different Accept headers to validate response formats

## Bugs list for [Swagger Petstore API](https://petstore.swagger.io/)

---

# Create user - This can only be done by the logged in user.

**Bug**: Creat user endpoint, allow creation of a user with the same user request body multiple times intead of returning an error
- **Ticket ID**: BR-001
- **Severity**: Major
- **Priority**: Medium
- **Steps to Reproduce**:
  1. Create a user with a specific credentials. e.g.
  ```json
  {
    "id": 54,
    "username": "john4kbvih4jvs",
    "firstName": "john4kbvih4jvs",
    "lastName": "john4kbvih4jvs",
    "email": "johnreb109eabrqJia",
    "password": "john4kbvih4jvs",
    "phone": "1111111111",
    "userStatus": 0
  }
  ```
  2. Repeat the request with the same user credentials
  3. Observe the response 
- **Expected Result**: The Create User endpoint should enforce uniqueness for user accounts. When attempting to create a user with existing credentials, it should return an appropriate error response (e.g., 409 Conflict) indicating that the user already exists. 
- **Actual Result**: The user is created successfully without any errors and returning 200 status code. Allowing duplicate users can cause data inconsistency.

---

**Bug**: Creat user endpoint, exhibits inconsistent behavior in ID assignment.
- **Ticket ID**: BR-002
- **Severity**: Major
- **Priority**: Medium
- **Steps to Reproduce**:
  1. Attempt to create a user with id = 0 or a negative number and observe the response.
  2. Create a user with a valid id value greater than 0 amd observe the response
- **Expected Result**: The system should return an error when an ID of 0 or a negative number is provided. Users should only be created with a valid, positive ID. 
- **Actual Result**: The system assigns a large number when the ID is 0 or negative, and IDs greater than 0 are assigned as expected, leading to inconsistent ID assignment. It can lead to data integrity issues.

---

**Bug**: Creat user endpoint, currently allows the creation of a new user without requiring authentication, which poses a significant security risk.
- **Ticket ID**: BR-003
- **Severity**: Critical
- **Priority**: High
- **Steps to Reproduce**:
  1. Attempt to create a new user without being logged in.
  2. Observe the response.
- **Expected Result**: The system should require user authentication and return a 401 Unauthorized or 403 Forbidden status when an unauthenticated request is made.
- **Actual Result**: The user is created successfully without any authentication required and rreturns 200 status code. Allowing unauthenticated user creation is a severe security flaw,

---

**Bug**: Create user endpoint, permits the creation of user even when  `id` and `userstatus`fields are provided as a string instead of an integer
- **Ticket ID**: BR-004
- **Severity**: Critical
- **Priority**: High
- **Steps to Reproduce**:
  1. Send a request to the user create endpoint with the following incorrect data types:
  ```json
  {
      "id": "1",
      "username": "johnvovva39embs",
      "firstName": "johnvovva39embs",
      "lastName": "johnvovva39embs",
      "email": "johnvovva39embs@gmail.com",
      "password": "johnvovva39embs",
      "phone": "1111111111",
      "userStatus": "23"
  }
  ```
  2. Observe the response.
- **Expected Result**: The API should validate input types and return an error message when incorrect data types are provided
- **Actual Result**: The API accepts the incorrect data types returns 200 status code  without validation and automatically converts them into their correct types , which can lead to data integrity issues and unexpected behavior in the application. Incorrect type handling is a severe issue that could lead to unpredictable behavior.

---

# **Bug**: Create User endpoint permits the creation of a user even when the `username`, `firstName`, `lastName`, `email`, `password`, and `phone` fields are provided as integers instead of strings.
- **Ticket ID**: BR-005
- **Severity**: Critical
- **Priority**: High
- **Steps to Reproduce**:
  1. Send a request to the User Create endpoint with the following incorrect data types:
  - Set the id field as a string (e.g., "123").
  - Set username, firstname, lastname, email, password, and phone fields as integers (e.g., 456).
  2. Observe the response.
- **Expected Result**: The API should validate input types and return an error message when incorrect data types are provided
- **Actual Result**: The API accepts the incorrect data types returns a 200 status code without validation and automatically converts them into their correct types , which can lead to data integrity issues and unexpected behavior in the application. Incorrect type handling is a severe issue that could lead to unpredictable behavior.

---

**Bug**: User create endpoint allows creating of a user with an invalid email address format
- **Ticket ID**: BR-006
- **Severity**: Major
- **Priority**: High
- **Steps to Reproduce**:
  1. Send a request to the User Create endpoint with an invalid email format e.g.
  ```json
  {
    "id": 54,
    "username": "john4kbvih4jvs",
    "firstName": "john4kbvih4jvs",
    "lastName": "john4kbvih4jvs",
    "email": "johnreb109eabrqJia",
    "password": "john4kbvih4jvs",
    "phone": "1111111111",
    "userStatus": 0
  }
  ```
  2. Observe the response.
- **Expected Result**: The API should validate the email format and return an error message indicating that the email address is not valid.
- **Actual Result**: The API allows the creation of a user returns 200 Status code even when the email address is not in a valid email format, potentially leading to issues with user identification and communication.

**Bug**: Create user endpoints allows creation of a user when required fields are missing in the request body. 
- **Ticket ID**: BR-007
- **Severity**: Major
- **Priority**: High
- **Steps to Reproduce**: 
  1. Send a request to the User Create endpoint with a request body that includes only the username field, such as:
  ```json 
  {
    "username": "johnvovva39embssds"
  }
  ```
  2. Observe ther response.
- **Expected Result**: The API should validate the request body and return an error message indicating that required fields are missing.
- **Actual Result**: The API returns a 200 status code and creates a user, even when required fields are missing from the body object. Missing field validation impacts the application’s data integrity.

--- 

**Bug**: Create user endpoint, allows assigning different ID to the same username 
- **Ticket ID**: BR-008
- **Severity**: Critical
- **Priority**: High
- **Steps to Reproduce**:
 1. Send a post request to the User Create endpoint with the following body:
     ```json
     {
       "id": "100",
       "username": "testUser1",
       "firstName": "johnwp36fc9ie58",
       "lastName": "johnwp36fc9ie58",
       "email": "johnwp36fc9ie58@gmail.com",
       "password": "johnwp36fc9ie58",
       "phone": "1111111111",
       "userStatus": 0
     }
     ```
  2. Send another POST request to the same endpoint with a different ID but the same username, for example:
    ```json
    {
      "id": "101",
      "username": "testUser1",
      "firstName": "johnwp36fc9ie58",
      "lastName": "johnwp36fc9ie58",
      "email": "johnwp36fc9ie58@gmail.com",
      "password": "johnwp36fc9ie58",
      "phone": "1111111111",
      "userStatus": 0
    }
    ```
  3. Observe the response
- **Expected Result**: The API should enforce uniqueness for usernames, preventing the creation of multiple users with the same username. An appropriate error message should be returned, indicating that the username already exists.
- **Actual Result**: The API returns a 200 status code for both requests, allowing the creation of users with the same username but different IDs, which can result in confusion in user management.

---

# update username - This can only be done by the logged in user.

**Bug**: Update user endpoint with parameter username, currently allows the updating an existing user without requiring authentication, which poses a significant security risk.
- **Ticket ID**: BR-009
- **Severity**: Critical
- **Priority**: High
- **Steps to Reproduce**:
  1. Attempt to create a update an existing user without being logged in.
  2. Observe the response.
- **Expected Result**: The system should require user authentication and return a 401 Unauthorized or 403 Forbidden status when an unauthenticated request is made.
- **Actual Result**: The user is updated successfully without any authentication required and returns 200 status code.

---

**Bug**: Update user endpoint with parameter username does not validate the `id` in the request body against the existing user. Instead, it either creates a new user or updates the existing user with a new id without raising an error.
- **Ticket ID**: BR-010
- **Severity**: Critical
- **Priority**: High
- **Steps to Reproduce**:
  1. Create a user with `id` and `username` lets say "1" and "john" respectively
  2. Send a `PUT` request to `https://petstore.swagger.io/v2/user/john` with the following body:
    ```json
    {
      "id": 2,
      "username": "john",
      "firstName": "string",
      "lastName": "string",
      "email": "string",
      "password": "string",
      "phone": "string",
      "userStatus": 0
    }
    ```
  3. Observe the response status code.
- **Expected Result**: - Either it should ignore the `id` field in the request body and update only the other fields, or
  - Return a validation error indicating that the `id` in the body must match the one used during the user's creation.
- **Actual Result**: A user gets updated with return of 200 status code.

---

**Bug**: Update user endpoint with parameter username, returning status `200` for non-existent username instead of a `404 Not Found` error.
- **Ticket ID**: BR-011
- **Severity**: Major
- **Priority**: Medium
- **Steps to Reproduce**:
  1. Send a Put request with the non-existent username.
  2. Observe the response status code.
- **Expected Result**:  The API should return a `404 User not found Internal Server Error` 
- **Actual Result**: The API returned `500 Internal Server Error`.

---

# getting username

**Bug**: Get user endpoint with parameter username, returns a `404 User Not Found` status for an empty or invalid username (e.g., using special characters like `*`, `!`, `()`, or `""`) instead of `400 Invalid username supplied`.
- **Ticket ID**: BR-012
- **Severity**: Major
- **Priority**: Medium
- **Steps to Reproduce**:
  1. Send a Get request with the invalid username.
  2. Observe the response status code.
- **Expected Result**:  The API should return a `400 Invalid username supplied` error indicating that the username is invalid.
- **Actual Result**: Returns `404 not found` status code

---

# delete username - This can only be done by the logged in user. 


**Bug**: Delete user endpoint with username parameter allows a user to delete their account without being logged in, which violates the expected authorization requirements.
- **Ticket ID**: BR-013
- **Severity**: Critical
- **Priority**: High
- **Steps to Reproduce**:
  1. Attempt to delete a user account without logging in.
  2. Observe the response status code.
- **Expected Result**: The API should return a `403 Forbidden` error indicating that only logged-in users can delete their accounts.
- **Actual Result**: The API allows the deletion of the user account without any authentication, potentially returning a `200` status code.

---

**Bug**: Delete user endpoint with parameter username, returns 404 Not Found status for invalid username instead of status 400 Invalid user supplied.
- **Ticket ID**: BR-014
- **Severity**: Medium
- **Priority**: Medium
- **Steps to Reproduce**:
  1. Send a delete user request with invalid username parameter. e.g.

  https://petstore.swagger.io/v2/user/
  
  2. Observe the response status code.
- **Expected Result**: The API should return a `400 Invalid Usersupplied` indicating that username is invalid
- **Actual Result**: The API returns a `404 Not Found` status code.

---

# user login
## Login without empty ormissing username or password or both
**Bug**: User login endpoint allows a user to login without providing a username or password or both, returning a `200` status code even when the credentials are missing. 
- **Ticket ID**: BR-015
- **Severity**: Critical
- **Priority**: High
- **Steps to Reproduce**:
  1. Send a login request using the following API call:
  https://petstore.swagger.io/v2/user/login?username=""&password=kumar 
  2. Observe the response status code.
- **Expected Result**: The API should return a `400 Invalid username/password or Bad Request` error indicating that both username and password are required.
- **Actual Result**: The API returns `200` status code, indicating a successful login even though credentials are missing.

---

# User logout
## letting the user logout without authorization session id 
**Bug**: User logout endpoint allows a user to logout without a valid session id, returning 200 status code instead of a 403 Forbidden.
- **Ticket ID**: BR-016
- **Severity**: Critical
- **Priority**: High
- **Steps to Reproduce**:
  1. Attempt to log out without providing a valid session ID.
  2. Observe the response
- **Expected Result**: The API should return a `403 Forbidden` error indicating that authorization is required to perform the logout operation.
- **Actual Result**: The API returns 200 status code with the following response. This may result in improper session management.
  ```json
  {
      "code": 200,
      "type": "unknown",
      "message": "ok"
  }
  ```
---

# Pet
Endpoints which requires OAuth2
add a pet 
Updating pet
find pet id
updates a pet
Pet delete endpoint api_key in header optional and authorization

# Pet assumption that ID needs to be unique

# adding a pet
## adding the pet without authorization

**Bug**: Add a new pet endpoint without any authorization returns 200 status code instead of a something like 403 Forbidden.
- **Ticket ID**: BR-017
- **Severity**: Critical
- **Priority**: High
- **Steps to Reproduce**:
  1. Attempt to add a pet without proper authorization.
  2. Observe the response
- **Expected Result**: The API should return a `403 Forbidden` error indicating that authorization is required to perform the add operation.
- **Actual Result**: Returns 200 status code

---

**Bug**: Add a new pet endpoint allows creation of duplicate pets, returning a `200` status code instead of an appropriate error code like `400 Bad Request`.
- **Ticket ID**: BR-018
- **Severity**: High
- **Priority**: Medium
- **Steps to Reproduce**:
  1. Send post request with specific pet data in the request bodye.g. 
  ```xml
  <?xml version="1.0" encoding="UTF-8"?>
  <Pet>
    <id>1</id>
    <Category>
      <id>0</id>
      <name>Dog</name>
    </Category>
    <name>Jimmy</name>
    <photoUrls>
      <photoUrl>string</photoUrl>
    </photoUrls>
    <tags>
      <Tag>
        <id>0</id>
        <name>string</name>
      </Tag>
    </tags>
    <status>available</status>
  </Pet>
  ```
  2. Attempt to create the same pet again
- **Expected Result**: The system should prevent duplicate pet and return a 409 Conflict or similar error message.
- **Actual Result**: The same pet is created successfully without any errors and getting 200 status code with response body 
  ```xml
  <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
  <Pet>
      <id>1</id>
      <name>Jimmy</name>
      <photoUrls>
          <photoUrl>string</photoUrl>
      </photoUrls>
      <status>available</status>
      <tags/>
  </Pet>
  ```
- **Comments**: Here the Content-Type and accept header was set to application/xml

---

**Bug**: Add a new pet endpoint allows creation of a pet when all the fields are missing in the request body. 
- **Ticket ID**: BR-019
- **Severity**: High
- **Priority**: Major
- **Steps to Reproduce**:
  1. sending 
  ```xml
  <?xml version="1.0" encoding="UTF-8"?>
  <Pet>
  </Pet>
  ```
- **Expected Result**: The API should validate the request body and return an error message indicating that required fields are missing.
- **Actual Result**: The API returns a 200 status code and creates a pet, even when required fields are missing from the body object. Missing field validation impacts the application’s data integrity.
```xml
  <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
  <Pet>
      <id>9223372016900019706</id>
      <photoUrls/>
      <tags/>
  </Pet>
```

---

# Delete a pet - Requires the OAuth2, implicit authorization

**Bug**: Delete pet endpoint with allows deletion without api key or authorization.
- **Ticket ID**: BR-020
- **Severity**: Critical
- **Priority**: High
- **Steps to Reproduce**:
  1. Attempt to delete a pet without providing an API key or proper authorization.
- **Expected Result**: The API should return a `403 Forbidden` error indicating that authorization is required to perform the delete operation.
- **Actual Result**: Returning 200 status code
  ```Json
  {
      "code": 200,
      "type": "unknown",
      "message": "9223372016900028029"
  }
  ```
---

**Bug**: Delete pet endpoint with parameter petId returns 404 status for invalid id instead of 400
- **Ticket ID**: BR-021
- **Severity**: Medium
- **Priority**: Low
- **Steps to Reproduce**:
  1. Send a DELETE request with an invalid ID (e.g., "abc" or special characters like ",$!").
  2. Observe the response
- **Expected Result**: The API should return a `400 Bad Request` error indicating that the ID is invalid.
- **Actual Result**: The api response is
  ```Json
  {
      "code": 404,
      "type": "unknown",
      "message": "java.lang.NumberFormatException: For input string: \"abcv\""
  }
  ```
--- 

# Find by pet id

**Bug**: Find pet endpoint with parameter petId without authorization returns 200 Status Code
- **Ticket ID**: BR-022
- **Severity**: Critical
- **Priority**: High
- **Steps to Reproduce**:
  1. Attempt to create a new user without being logged in.
  2. Observe the response.
- **Expected Result**: The system should require user authentication and return a 401 Unauthorized or 403 Forbidden status when an unauthenticated request is made.
- **Actual Result**: The endpoint returns a `200` status code, allowing access to pet information without authorization. 

---

# update existing pet

**Bug**: Update an existing pet end point retuns 200 status code for non-existent pet instead of getting something like 404 Not found error
- **Ticket ID**: BR-023
- **Severity**: High
- **Priority**: Medium
- **Steps to Reproduce**:
1. To make sure pet does not exist, delete the Pet id e.g. 999
2. Send a PUT request using the same pet id from step 1  e.g. 999 with the XML payload e.g. 
  ```xml
  <?xml version="1.0" encoding="UTF-8"?>
  <Pet>
    <id>999</id>
    <Category>
      <id>0</id>
      <name>string</name>
    </Category>
    <name>Tom</name>
    <photoUrls>
      <photoUrl>string</photoUrl>
    </photoUrls>
    <tags>
      <Tag>
        <id>0</id>
        <name>string</name>
      </Tag>
    </tags>
    <status>available</status>
  </Pet>
  ```
- **Expected Result**: 404 Not Found error should be returned.
- **Actual Result**: API returns 
  ```xml
  <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
  <Pet>
      <id>999</id>
      <name>Tom</name>
      <photoUrls>
          <photoUrl>string</photoUrl>
      </photoUrls>
      <status>available</status>
      <tags/>
  </Pet>
  ```
- **Comments**: Here the Content-Type and accept header was set to application/xml

--------------------------------------------------

# Assumptions
1. The server generates the user `id` automatically if it's not provided or set to `0`. This is considered standard behavior for server-side ID generation.
2. assumption for the new user is that every user needs to have unique username as we have usernam get user by username and update user by username 
3. There are parameters which are marked with * are required and other fields can be missed or left blank or don't need to put in the request body or header

3. Data type validation issues exist, such as allowing integers for string fields (e.g., `username`, `firstName`) and strings for integer fields (e.g., `id`).
4. Missing fields in the request body do not cause validation errors.

