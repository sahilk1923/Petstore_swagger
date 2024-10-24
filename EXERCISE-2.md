# Objective
The objective of this exercise was to implement automated tests for the [Swagger Petstore API](https://petstore.swagger.io/), focusing on creating, modifying, and deleting data through the API. Not all endpoints were tested exhaustively. Instead, key endpoints were chosen to cover important aspects of API behavior such as:

- **HTTP Status Code Validation**: Ensuring the API returns appropriate status codes
- **Authentication**: Testing user session management and authentication mechanisms, including validation of API key and OAuth2 authentication.
- **Data Validation**: Proper information handling, sending correct and incorrect data to validate that the API handles both valid and invalid inputs appropriately.
- **Response Body Validation**: Ensuring the response body contains expected data and appropriate error messages.
- **Edge cases**: Testing scenarios with null values, incorrect formats, and missing fields to ensure the API responds gracefully.

The tests were written using Python and pytest, alongside manual testing using Postman.

## Covered Endpoints:
- **User**:
  - Creating a user
  - Updating a user (by username)
  - Deleting a user (by username)
  - Retrieving a user (by username)

- **Pet**:
  - Adding a new pet
  - Updating an existing pet
  - Retrieving a pet (by ID)
  - Deleting a pet (by ID)


## Known Limitations
- **Partial Endpoint Coverage**: Not all available API endpoints were tested. The selection was made to focus on essential areas such as user authentication, session handling, and data manipulation. Additional tests could be implemented to further extend coverage.
- **Edge Cases**: While some edge cases were tested, more complex test scenarios could be added in future iterations (e.g., stress testing and performance testing).

## Further Improvements
Future enhancements to the automated tests can include:
- Expanding the test coverage to remaining API endpoints functionality.
- Additional Edge Case Testing can be done : For example, testing with null or empty values in the request body, different content type,or testing unsupported HTTP methods.
- Performance Testing: Adding tests to validate the performance and response times of API calls under heavy load.
- Security Testing can be done


## Test Scenarios Implemented
The test cases include, but are not limited to, the following scenarios:

## User API Tests:
Create User with Valid Data: Ensure the user is created successfully with a valid JSON payload.
Create User with Invalid Data: Test the API’s behavior when sending invalid data (e.g., incorrect username format, non-string email).
Fetch User by Username: Validate that an existing user can be fetched by username.
Update User with Valid/Invalid Data: Check both successful updates and the API’s response to invalid data during user updates.
Delete User: Ensure that an existing user can be deleted and that non-existent users return the appropriate error.
Pet API Tests:
Add Pet with Valid Data: Add a pet with valid XML data and verify the response.
Find Pet by Invalid ID: Test the response when fetching a pet with an invalid or non-existent ID.
Update Pet with Incorrect Data: Test updating a pet with incorrect data formats.
Delete Pet: Ensure a pet can be deleted and verify the API's behavior when attempting to delete a non-existent pet.

## Test Results:
Test results will be output to the terminal, showing the status of each test (e.g., PASS/FAIL) along with any relevant details such as response codes and validation errors.


