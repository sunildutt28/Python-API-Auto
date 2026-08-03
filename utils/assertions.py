def assert_status_code(response, expected_status):
    assert response.status_code == expected_status, (
        f"Expected status code {expected_status}, "
        f"but got {response.status_code}"
    )


def assert_json_key(response, key):
    json_data = response.json()
    assert key in json_data, (
        f"'{key}' not found in response"
    )