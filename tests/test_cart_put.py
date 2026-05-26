import pytest

from utils.api_client import APIClient

from utils.assertions import (
    assert_status_code,
    assert_response_not_empty
)


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.api
def test_update_cart():

    payload = {
        "userId": 1,
        "date": "2026-05-26",
        "products": [
            {
                "productId": 2,
                "quantity": 5
            }
        ]
    }

    response = APIClient.put("/carts/1", payload)

    assert_status_code(response, 200)

    data = response.json()

    assert_response_not_empty(data)

    assert data["userId"] == 1, (
        "User ID in response does not match expected value"
    )

    assert data["products"][0]["productId"] == 2, (
        "Updated product ID does not match expected value"
    )


@pytest.mark.regression
@pytest.mark.api
def test_update_cart_with_invalid_id():

    payload = {
        "userId": 1,
        "date": "2026-05-26",
        "products": [
            {
                "productId": 1,
                "quantity": 1
            }
        ]
    }

    response = APIClient.put("/carts/9999", payload)

    assert response.status_code in [200, 400, 404], (
        f"Expected status code 200, 400, or 404, "
        f"but got {response.status_code}"
    )