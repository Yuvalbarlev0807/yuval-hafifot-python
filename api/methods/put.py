from api.data.request_body import PUT_REQUEST_BODY
from api.data.testData import headers, url
from api.utils.requestsFunctions import put_request


def test_change_product_name():
    response = put_request(headers,f"{url["base_url"]}/products/1",PUT_REQUEST_BODY)
    data = response.json()
    assert response.status_code == 200
    assert data["title"] == "iPhone Galaxy +1"
    print(data)
    print(response.status_code)