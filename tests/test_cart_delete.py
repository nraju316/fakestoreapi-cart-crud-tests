import pytest

from utils.api_client import APIClient

from utils.assertions import (
    assert_status_code,
    assert_response_not_empty
)


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.api
def test_delete_cart():

    response = APIClient.delete("/carts/1")

    assert_status_code(response, 200)

    data = response.json()

    assert_response_not_empty(data)

    assert "id" in data, (
        "Deleted cart response does not contain 'id'"
    )


@pytest.mark.regression
@pytest.mark.api
def test_delete_invalid_cart():

    response = APIClient.delete("/carts/9999")

    assert response.status_code in [200, 404], (
        f"Expected status code 200 or 404, "
        f"but got {response.status_code}"
    )