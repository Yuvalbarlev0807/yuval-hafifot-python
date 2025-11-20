import pytest
from api.Pytest.data.testData import headers
from api.Pytest.utils.requestsFunctions import post_request


@pytest.fixture(scope="module")
def post_request_body():
    # לא באמת מייצג את המטרה של ה scope אבל אין פה יותר מדי איך להשתמש בו בצורה נכונה
    return {
        "title": "yuval",
        "price": 12,

    }
def test_add_product(base_url,post_request_body):
    response = post_request(headers, f"{base_url}/products/add", post_request_body)
    data = response.json()
    assert response.status_code == 201
    assert data["title"] == "yuval"
    assert "id" in data
    print(response.status_code)
    print(data)
