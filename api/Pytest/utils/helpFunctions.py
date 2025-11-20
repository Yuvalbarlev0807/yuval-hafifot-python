from api.Pytest.data.testData import url
from api.Pytest.methods.conftest import base_url
from api.Pytest.utils.requestsFunctions import get_request


def verify_product_exists(product_id, base_url):
    try:
        response = get_request(f"{base_url}/products/{product_id}")
        data = response.json()
        return data.get("id") == product_id
    except Exception as e:
        print(f"verify_product_exists failed: {e}")
        return False


def get_all_products_categories():
    response = get_request(f'{url["base_url"]}/products/category-list')
    print(response.json())
    return response

