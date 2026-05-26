import pytest

from utils.api_client import APIClient

from utils.assertions import (
    assert_status_code,
    assert_key_exists,
    assert_response_not_empty,
    assert_response_time
)


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.api
def test_get_single_cart():

    response = APIClient.get("/carts/1")

    assert_status_code(response, 200)

    assert_response_time(response, 3)

    data = response.json()

    assert_response_not_empty(data)

    assert_key_exists(data, "id")
    assert_key_exists(data, "userId")
    assert_key_exists(data, "products")


@pytest.mark.regression
@pytest.mark.api
def test_get_all_carts():

    response = APIClient.get("/carts")

    assert_status_code(response, 200)

    data = response.json()

    assert_response_not_empty(data)

    assert isinstance(data, list), (
        "Expected response to be a list"
    )

    assert len(data) > 0, (
        "Cart list is empty"
    )


@pytest.mark.regression
@pytest.mark.api
def test_get_invalid_cart():

    response = APIClient.get("/carts/9999")

    assert response.status_code in [200, 404], (
        f"Expected status code 200 or 404, "
        f"but got {response.status_code}"
    )


@pytest.mark.regression
@pytest.mark.api
def test_get_carts_by_user():

    response = APIClient.get("/carts/user/1")

    assert_status_code(response, 200)

    data = response.json()

    assert_response_not_empty(data)

    assert isinstance(data, list), (
        "Expected user carts response to be a list"
    )


@pytest.mark.regression
@pytest.mark.api
def test_get_cart_content_type():

    response = APIClient.get("/carts/1")

    assert "application/json" in response.headers["Content-Type"], (
        "Response Content-Type is not application/json"
    )