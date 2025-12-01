import requests

from framework.common import get_app_config


class PublicAPI:

    endpoints = {
        'get_products': 'api/productsList',
        'search_product': 'api/searchProduct',
        'create_user': 'api/createAccount',
        'update_user': 'api/updateAccount',
        'delete_user': 'api/deleteAccount'
    }

    def __init__(self):
        self.config = get_app_config()
        self.host = self.config.get('platform').get('url')

    def get_products(self, status_code: int = 200):
        response = requests.get(
            url=f'{self.host}{self.endpoints['get_products']}'
        )

        assert (
                response.status_code == status_code
        ), 'Response code is incorrect'

        return response.json()

    def search_product(self, body: dict, status_code: int = 200):
        response = requests.post(
            url=f'{self.host}{self.endpoints['search_product']}',
            data=body
        )

        assert (
                response.status_code == status_code
        ), 'Response code is incorrect'

        return response.json()

    def create_user(self, body: dict, status_code: int = 200):
        response = requests.post(
            url=f'{self.host}{self.endpoints['create_user']}',
            data=body
        )

        assert (
                response.status_code == status_code
        ), 'Response code is incorrect'

        return response.json()

    def update_user(self, body: dict, status_code: int = 200):
        response = requests.put(
            url=f'{self.host}{self.endpoints['update_user']}',
            data=body
        )

        assert (
                response.status_code == status_code
        ), 'Response code is incorrect'

        return response.json()

    def delete_user(self, email: str, password: str, status_code: int = 200):
        response = requests.delete(
            url=f'{self.host}{self.endpoints['delete_user']}',
            data={'email': email, 'password': password}
        )

        assert (
                response.status_code == status_code
        ), 'Response code is incorrect'

        return response.json()
