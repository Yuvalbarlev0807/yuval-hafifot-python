import pytest

from api.Pytest.methods.conftest import base_url
from api.Pytest.utils.helpFunctions import verify_product_exists, get_all_products_categories
from api.Pytest.utils.requestsFunctions import get_request

categories = get_all_products_categories().json()


def test_get_all_products(base_url):
    response = get_request(f"{base_url}/products")
    data = response.json()
    products = data["products"]
    assert response.status_code == 200
    assert all("id" in product for product in products)
    print(response.status_code)
    print(data)



@pytest.mark.parametrize(
    "product_id, expected_status,expected_validation_state",
    [

        pytest.param(1, 200, True),
        pytest.param(1234, 404, False, marks=pytest.mark.skip(reason="עושה סקיפ על מוצר לא קיים"))
    ],
)
def test_get_product_by_id(base_url, product_id, expected_status, expected_validation_state):
    response = get_request(f"{base_url}/products/{product_id}")
    data = response.json()
    assert response.status_code == expected_status
    assert (verify_product_exists(product_id, base_url)) == expected_validation_state
    print(data)
    print(response.status_code)




@pytest.mark.parametrize("category", categories)
def test_get_products_category(base_url, category):
    response = get_request(f"{base_url}/products/category/{category}")
    data = response.json()
    assert response.status_code == 200
    assert all(item["category"] == category for item in data["products"])
    print(data)
    print(response.status_code)




def test_get_all_products_categories():
    response = get_all_products_categories()
    assert response.status_code == 200
    print(response.json())
