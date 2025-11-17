from api.data.testData import headers, url
from api.utils.requestsFunctions import delete_request


def test_delete_product():
    response = delete_request(headers, f"{url["base_url"]}/products/1")
    data = response.json()
    assert data["isDeleted"] == True
    assert data["id"] == 1
    assert response.status_code == 200
    print(response.status_code)
    print(data)
