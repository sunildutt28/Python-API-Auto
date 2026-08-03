from api.client import APIClient

from utils.assertions import assert_status_code

from api.endpoints import Endpoints

def test_get_user(api_client):

    response = api_client.get(Endpoints.user_by_id(1))

    assert_status_code(response, 200)

    user = response.json()

    assert user["id"] == 1