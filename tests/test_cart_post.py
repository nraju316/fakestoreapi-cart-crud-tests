from copy import deepcopy

import pytest

from utils.api_client import APIClient

from utils.assertions import (
    assert_status_code,
    assert_response_not_empty,
    assert_response_time
)


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.api
def test_create_cart(sample_cart_payload):

    response = APIClient.post(
        "/carts",
        sample_cart_payload
    )

    assert_status_code(response, 201)

    assert_response_time(response, 3)

    data = response.json()

    assert_response_not_empty(data)

    assert data["userId"] == 1, (
        "User ID in response does not match expected value"
    )

    assert len(data["products"]) > 0, (
        "Products list is empty in response"
    )


@pytest.mark.regression
@pytest.mark.api
@pytest.mark.xfail(reason="API accepts empty products list")
def test_create_cart_with_empty_products(sample_cart_payload):

    payload = deepcopy(sample_cart_payload)

    payload["products"] = []

    response = APIClient.post("/carts", payload)

    assert response.status_code == 400, (
        f"Expected status code 400, "
        f"but got {response.status_code}"
    )


@pytest.mark.regression
@pytest.mark.api
@pytest.mark.xfail(reason="API accepts payload with missing fields")
def test_create_cart_without_user_id(sample_cart_payload):

    payload = deepcopy(sample_cart_payload)

    del payload["userId"]

    response = APIClient.post("/carts", payload)

    assert response.status_code == 400, (
        f"Expected status code 400, "
        f"but got {response.status_code}"
    )