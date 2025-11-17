
from api.data.request_body import POST_REQUEST_BODY
from api.data.testData import url, headers
from api.utils.requestsFunctions import post_request


def test_add_product():
    response = post_request(headers, f"{url["base_url"]}/products/add", POST_REQUEST_BODY)
    data = response.json()
    assert response.status_code == 201
    assert data["title"] =="BMW Pencil"
    assert "id" in data
    print(response.status_code)
    print(data)