import pytest
from utils.api_client import ApiClient
from utils.config import BASE_URL, HEADERS, HEADERS1

client = ApiClient(BASE_URL)

@pytest.fixture
def create_order():
    data = {
        "id": 123,
        "petId": 12345,
        "quantity": 2,
        "shipDate": "2024-10-21T13:00:00.000Z",
        "status": "placed",
        "complete": True
    }
    response = client.post("/store/order", data,HEADERS)
    return response

def test_create_order(create_order):
    assert create_order.status_code == 200
    assert create_order.json()["status"] == "placed"

def test_get_order_by_id():
    response = client.get("/store/order/123",HEADERS)

    assert response.status_code == 200
    assert response.json()["id"] == 123

def test_delete_order_by_id():
    response = client.delete("/store/order/123",HEADERS)
    assert response.status_code == 200