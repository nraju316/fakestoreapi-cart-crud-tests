import requests

from utils.config import BASE_URL, HEADERS


class APIClient:

    @staticmethod
    def get(endpoint):

        try:
            response = requests.get(
                f"{BASE_URL}{endpoint}",
                headers=HEADERS,
                timeout=10
            )

            return response

        except requests.exceptions.RequestException as e:
            print(f"GET request failed: {e}")
            raise

    @staticmethod
    def post(endpoint, payload=None):

        try:
            response = requests.post(
                f"{BASE_URL}{endpoint}",
                json=payload,
                headers=HEADERS,
                timeout=10
            )

            return response

        except requests.exceptions.RequestException as e:
            print(f"POST request failed: {e}")
            raise

    @staticmethod
    def put(endpoint, payload=None):

        try:
            response = requests.put(
                f"{BASE_URL}{endpoint}",
                json=payload,
                headers=HEADERS,
                timeout=10
            )

            return response

        except requests.exceptions.RequestException as e:
            print(f"PUT request failed: {e}")
            raise

    @staticmethod
    def delete(endpoint):

        try:
            response = requests.delete(
                f"{BASE_URL}{endpoint}",
                headers=HEADERS,
                timeout=10
            )

            return response

        except requests.exceptions.RequestException as e:
            print(f"DELETE request failed: {e}")
            raise