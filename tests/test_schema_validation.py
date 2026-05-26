import json
import pytest

from jsonschema import validate

from utils.api_client import APIClient

from utils.assertions import (
    assert_status_code
)


@pytest.mark.schema
@pytest.mark.regression
@pytest.mark.api
def test_cart_response_schema():

    response = APIClient.get("/carts/1")

    assert_status_code(response, 200)

    assert (
        response.headers["Content-Type"]
        == "application/json; charset=utf-8"
    ), (
        "Cart response Content-Type is incorrect"
    )

    response_json = response.json()

    with open("schemas/cart_schema.json") as file:
        schema = json.load(file)

    validate(
        instance=response_json,
        schema=schema
    )


@pytest.mark.schema
@pytest.mark.regression
@pytest.mark.api
def test_login_response_schema():

    payload = {
        "username": "mor_2314",
        "password": "83r5^_"
    }

    response = APIClient.post("/auth/login", payload)

    assert_status_code(response, 201)

    assert (
        response.headers["Content-Type"]
        == "application/json; charset=utf-8"
    ), (
        "Login response Content-Type is incorrect"
    )

    response_json = response.json()

    with open("schemas/login_schema.json") as file:
        schema = json.load(file)

    validate(
        instance=response_json,
        schema=schema
    )


@pytest.mark.schema
@pytest.mark.regression
@pytest.mark.api
def test_product_response_schema():

    response = APIClient.get("/products/1")

    assert_status_code(response, 200)

    assert (
        response.headers["Content-Type"]
        == "application/json; charset=utf-8"
    ), (
        "Product response Content-Type is incorrect"
    )

    response_json = response.json()

    with open("schemas/product_schema.json") as file:
        schema = json.load(file)

    validate(
        instance=response_json,
        schema=schema
    )