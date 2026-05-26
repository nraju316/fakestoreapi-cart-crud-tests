import json


def print_response(response):

    print("\nStatus Code:", response.status_code)

    try:
        print(
            json.dumps(
                response.json(),
                indent=4
            )
        )

    except Exception:
        print(response.text)