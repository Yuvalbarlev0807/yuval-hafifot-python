import requests

from api.GraphQL.data.test_data import variables_update_post, url
from api.GraphQL.queries.update_quries import update_post_query


def test_update_post():
    response=requests.post(url,json={"query":update_post_query,"variables": variables_update_post})
    data = response.json()
    post = data["data"]["updatePost"]
    assert "id" in post
    assert post["body"] == "changed body"
    assert response.status_code == 200

    print(data)