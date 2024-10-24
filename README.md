# SWAGGER_PETSTORE API Testing
## Project Structure

```plaintext
SWAGGER_PETSTORE/
├── tests/                 # Folder containing automated test scripts for the Petstore API
│   ├── test_user.py       # Test cases for user
│   ├── test_store.py      # Test cases for deleting a pet by ID
├── utils/                 # Utility folder for helper functions used in the tests
│   └── api_client.py      # Helper functions for making API requests and handling 
│   └── config.py          # Stores API configuration settings.
├── data/
│   └──user_data.py        # Test data for user
├── pytest.ini             # Pytest configuration
├── README.md              # Instructions and general overview of the project
├── EXERCISE-2.md          # About this activity 
├── BUGREPORT-2.md         # Documentation of found bugs with severity, priority, and details
├── requirements.txt       # List of Python dependencies required for running the tests
├── Postman_Collection/    # Collection file for postman 
│   └── PetStore_JSON_Us.. # Collection for user endpoints
│   └── PetStore_XML_Pet.. # Collection for pet endpoints
```

# Petstore API Test Automation

## Prerequisites
Before setting up and running the project, ensure that you have the following tools installed:

- Python 3.10.2
- pip (Python package installer) 24.2
- Visual Studio Code (or any other IDE, optional)

***Note**: The instructions in this document were verified on windows 11.*

## Overview
This project contains automated tests for the Petstore Swagger API. The tests cover creating, modifying, deleting pets, and uploading images.

### Setup Instructions
1. Clone the repository.
- ``git clone https://github.com/yourusername/sauce_demo_automation.git``
- ``cd sauce_demo_automation``
2. Create and Activate Virtual Environment
- ``python -m venv venv``
3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
4. To run tests
- To run all tests 
  ```
  pytest
  ```
  ***Note**: Running all tests is not recommended at this stage as some components are still under development and may not function as expected.*
- To run a specific test file (e.g., login tests):
  ```
  pytest tests/test_login.py
  ```
- To run the test with verbose output: (e.g., product listing tests):
  ```
  pytest --verbose  test_product_listing.py
  ```
- To run the test with detailed output with full tracebacks:
  ```
  pytest --tb=long
  ```

## Tests Implemented
- Creating a user
- Get a user
- Delete user
- User login

## Postman
There are two postman Collection files can be imported in postman to test the user and api API endpoints
