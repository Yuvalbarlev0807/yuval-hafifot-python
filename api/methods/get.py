import pytest

from api.utils.helpFunctions import verify_product_exists
from api.utils.requestsFunctions import get_request


@pytest.fixture(scope="module")
def product_id():
    return 5

def test_get_all_products(base_url):
    response = get_request(f"{base_url}/products")
    data = response.json()
    products = data["products"]
    assert response.status_code == 200
    assert all("id" in product for product in products)
    print(response.status_code)
    print(data)


def test_get_product_by_id(base_url,product_id):
    response = get_request(f"{base_url}/products/{product_id}")
    data = response.json()
    assert response.status_code == 200
    verify_product_exists(5)
    print(data)

def test_get_product_categories(base_url):
    response = get_request(f"{base_url}/products/categories")
    data = response.json()
    assert response.status_code == 200
    assert all("slug" in item for item in data)
    print(data)