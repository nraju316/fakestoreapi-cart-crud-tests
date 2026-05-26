import pytest

from utils.api_client import APIClient

from utils.assertions import (
    assert_status_code,
    assert_response_not_empty,
    assert_response_time
)

from utils.config import (
    VALID_USERNAME,
    VALID_PASSWORD
)


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.api
def test_login_with_valid_credentials():

    payload = {
        "username": VALID_USERNAME,
        "password": VALID_PASSWORD
    }

    response = APIClient.post("/auth/login", payload)

    assert_status_code(response, 201)

    assert_response_time(response, 3)

    data = response.json()

    assert_response_not_empty(data)

    assert "token" in data, (
        "Authentication token not found in response"
    )

    token = data["token"]

    assert isinstance(token, str), (
        "Token should be a string"
    )

    assert len(token) > 20, (
        "Token length is shorter than expected"
    )

    assert token.count(".") == 2, (
        "Token does not appear to be a valid JWT format"
    )


@pytest.mark.regression
@pytest.mark.api
def test_login_with_invalid_credentials():

    payload = {
        "username": "wrong_user",
        "password": "wrong_password"
    }

    response = APIClient.post("/auth/login", payload)

    assert response.status_code in [401, 400], (
        f"Expected 401 or 400 status code, "
        f"but got {response.status_code}"
    )


@pytest.mark.performance
@pytest.mark.api
def test_login_response_time():

    payload = {
        "username": VALID_USERNAME,
        "password": VALID_PASSWORD
    }

    response = APIClient.post(
        "/auth/login",
        payload
    )

    assert_response_time(response, 3)