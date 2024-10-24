# utils/api_helpers.py

import requests
# from tests.conftest import BASE_URL, HEADERS



class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def post(self, endpoint, data,HEADERS=None):
        try:
            url = f"{self.base_url}{endpoint}"
            response = requests.post(url, json=data,headers=HEADERS)
            print(f"post Status Code: {response.status_code}")
            print(f"post Response Body: {response.text}")
            print(f"post Response headers: {response.headers }")
            return response
        except requests.exceptions.Timeout:
            print("The request timed out.")
            return None
        except requests.exceptions.TooManyRedirects:
            print("The URL was bad. Please check the URL.")
            return None
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def get(self, endpoint,HEADERS=None):
        try:
            url = f"{self.base_url}{endpoint}"
            response = requests.get(url,headers=HEADERS)
            print(f"Get Status Code: {response.status_code}")
            print(f"get Response Body: {response.text}")
            print(f"get Response headers: {response.headers }")
            return response
        except requests.exceptions.Timeout:
            print("The request timed out.")
            return None
        except requests.exceptions.TooManyRedirects:
            print("The URL was bad. Please check the URL.")
            return None
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def delete(self, endpoint,HEADERS=None):
        try:
            url = f"{self.base_url}{endpoint}"
            response = requests.delete(url,headers=HEADERS)
            print(f"delete Status Code: {response.status_code}")
            print(f"delete Response Body: {response.text}")
            print(f"delete Response headers: {response.headers }")
            return response
        except requests.exceptions.Timeout:
            print("The request timed out.")
            return None
        except requests.exceptions.TooManyRedirects:
            print("The URL was bad. Please check the URL.")
            return None
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None
        
    def put(self, endpoint,HEADERS=None):
        try:
            url = f"{self.base_url}{endpoint}"
            response = requests.put(url,headers=HEADERS)
            print(f"put Status Code: {response.status_code}")
            print(f"put Response Body: {response.text}")
            print(f"put Response headers: {response.headers }")
            return response
        except requests.exceptions.Timeout:
            print("The request timed out.")
            return None
        except requests.exceptions.TooManyRedirects:
            print("The URL was bad. Please check the URL.")
            return None
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    # def post_request(endpoint, data):
    #     """Send a POST request."""
    #     response = requests.post(f"{BASE_URL}{endpoint}", json=data, headers=HEADERS)
    #     return response

    # def put_request(endpoint, data):
    #     """Send a PUT request."""
    #     response = requests.put(f"{BASE_URL}{endpoint}", json=data, headers=HEADERS)
    #     return response

    # def delete_request(endpoint):
    #     """Send a DELETE request."""
    #     response = requests.delete(f"{BASE_URL}{endpoint}", headers=HEADERS)
    #     return response

    # def assert_status_code(response, expected_status_code):
    #     """Check if the status code is as expected."""
    #     assert response.status_code == expected_status_code, (
    #         f"Expected {expected_status_code}, but got {response.status_code}."
    #     )