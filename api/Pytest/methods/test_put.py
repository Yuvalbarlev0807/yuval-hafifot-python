import pytest

from api.Pytest.data.testData import headers
from api.Pytest.utils.helpFunctions import verify_product_exists
from api.Pytest.utils.requestsFunctions import put_request


@pytest.fixture(scope="function")
def put_request_body():
    # באידיאל הייתי רוצה ליצור פה מוצר ואז להנגיש אותו בטסט על מנת לשנות אבל זה לא שומר באמת את הנתונים
    return {"title": "iPhone Galaxy +1", }


@pytest.fixture(scope="module")
def product_id(base_url):
    verify_product_exists(5, base_url)
    return 5


def test_change_product_name(base_url, product_id, put_request_body):
    response = put_request(headers, f"{base_url}/products/{product_id}", put_request_body)
    data = response.json()
    assert response.status_code == 200
    assert data["title"] == "iPhone Galaxy +1"
    print(data)
    print(response.status_code)
