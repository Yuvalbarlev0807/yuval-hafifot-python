import pytest

from api.data.testData import url
from api.utils.requestsFunctions import get_request


# @pytest.fixture(scope="session")
# def initial_connection():
# get_request(url["base_url"])


def test_get_all_products():
    response = get_request(f"{url["base_url"]}/products")
    data = response.json()
    products = data["products"]
    assert response.status_code == 200
    assert all("id" in product for product in products)
    print(response.status_code)
    print(data)


def test_get_product_by_id():
    response = get_request(f"{url["base_url"]}/products/1")
    data = response.json()
    assert response.status_code == 200
    assert "id" in data
    print(data)

def test_get_product_categories():
    response = get_request(f"{url["base_url"]}/products/categories")
    data = response.json()
    assert response.status_code == 200
    assert all("slug" in item for item in data)
    print(data)