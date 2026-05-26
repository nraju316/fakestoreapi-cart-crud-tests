import json
import pytest

from utils.api_client import APIClient

from utils.assertions import (
    assert_status_code,
    assert_response_not_empty
)


@pytest.mark.schema
@pytest.mark.regression
@pytest.mark.api
def test_product_snapshot_contract():

    response = APIClient.get("/products/1")

    assert_status_code(response, 200)

    current_response = response.json()

    assert_response_not_empty(current_response)

    with open("snapshots/product_snapshot.json") as file:
        snapshot = json.load(file)

    assert (
        set(current_response.keys())
        == set(snapshot.keys())
    ), (
        "Product response contract does not match snapshot structure"
    )