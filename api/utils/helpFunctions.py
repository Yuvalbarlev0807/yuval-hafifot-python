from api.data.testData import url
from api.utils.requestsFunctions import get_request


def verify_product_exists(product_id):
    response = get_request(f'{url["base_url"]}/products/{product_id}')
    data = response.json()
    assert data["id"] == product_id
