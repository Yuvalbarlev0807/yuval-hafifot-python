import pytest

from api.utils.requests import get_request


def test_get_all_products():
    response = get_request("https://dummyjson.com/products")
    assert response.status_code == 200
    print(response.status_code)
    print(response.text)