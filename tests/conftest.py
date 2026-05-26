import pytest
    
@pytest.fixture
def sample_cart_payload():

    return {
        "userId": 1,
        "date": "2026-05-26",
        "products": [
            {
                "productId": 1,
                "quantity": 2
            }
        ]
    }