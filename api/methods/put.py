import pytest

from api.data.request_body import PUT_REQUEST_BODY
from api.data.testData import headers
from api.utils.helpFunctions import verify_product_exists
from api.utils.requestsFunctions import put_request



@pytest.fixture(scope="module")
def product_id():
    verify_product_exists(5)
    return 5

def test_change_product_name(base_url,product_id):
    response = put_request(headers,f"{base_url}/products/{product_id}",PUT_REQUEST_BODY)
    data = response.json()
    assert response.status_code == 200
    assert data["title"] == "iPhone Galaxy +1"
    print(data)
    print(response.status_code)