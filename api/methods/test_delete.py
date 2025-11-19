import pytest

from api.data.testData import headers
from api.utils.helpFunctions import verify_product_exists
from api.utils.requestsFunctions import delete_request


@pytest.fixture(scope="module")
def product_id(base_url):
    # גם  פה באידיאל הייתי רוצה ליצור מוצר ואז להשתמש במזהה שלו בטסטים, אבל זה לא מתאפשר
    verify_product_exists(1, base_url)
    return "1"


def test_delete_product(base_url, product_id):
    response = delete_request(headers, f"{base_url}/products/{product_id}")
    data = response.json()
    assert data["isDeleted"] == True
    assert data["id"] == 1
    assert response.status_code == 200
    print(response.status_code)
    print(data)
