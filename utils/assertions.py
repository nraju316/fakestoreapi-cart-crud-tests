def assert_status_code(response, expected_status):

    assert response.status_code == expected_status, (
        f"Expected status code {expected_status}, "
        f"but got {response.status_code}"
    )


def assert_key_exists(response_json, key):

    assert key in response_json, (
        f"Key '{key}' not found in response"
    )


def assert_response_not_empty(response_json):

    assert response_json is not None
    assert response_json != {}
    assert response_json != []


def assert_product_count(products, expected_count):

    assert len(products) == expected_count, (
        f"Expected {expected_count} products, "
        f"but got {len(products)}"
    )


def assert_response_time(response, max_seconds):

    response_time = response.elapsed.total_seconds()

    assert response_time < max_seconds, (
        f"Response time {response_time}s exceeded "
        f"{max_seconds}s"
    )