import pytest

from utils.api_client import APIClient

from utils.assertions import (
    assert_status_code,
    assert_response_not_empty
)


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.api
@pytest.mark.parametrize(
    "product_id",
    [1, 2, 3, 5]
)
def test_create_cart_with_multiple_product_ids(product_id):

    payload = {
        "userId": 1,
        "date": "2026-05-26",
        "products": [
            {
                "productId": product_id,
                "quantity": 2
            }
        ]
    }

    response = APIClient.post("/carts", payload)

    assert_status_code(response, 201)

    data = response.json()

    assert_response_not_empty(data)

    assert data["products"][0]["productId"] == product_id, (
        f"Expected product ID {product_id}, "
        f"but got {data['products'][0]['productId']}"
    )

    assert data["products"][0]["quantity"] == 2, (
        "Product quantity does not match expected value"
    )