import requests

from config.settings import BASE_URL
from utils.logger import logger


class APIClient:

    def get(self, endpoint, **kwargs):

        url = f"{BASE_URL}{endpoint}"

        logger.info(f"GET {url}")

        response = requests.get(url, **kwargs)

        logger.info(f"Status Code : {response.status_code}")
        logger.info(f"Response Time : {response.elapsed.total_seconds()*1000:.0f} ms")

        return response

    def post(self, endpoint, **kwargs):
        url = f"{BASE_URL}{endpoint}"
        logger.info(f"POST {url}")
        response = requests.post(url, **kwargs)
        return response

    def put(self, endpoint, **kwargs):
        url = f"{BASE_URL}{endpoint}"
        logger.info(f"PUT {url}")
        response = requests.put(url, **kwargs)
        return response

    def delete(self, endpoint, **kwargs):
        url = f"{BASE_URL}{endpoint}"
        logger.info(f"DELETE {url}")
        response = requests.delete(url, **kwargs)
        return response