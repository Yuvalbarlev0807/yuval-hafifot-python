import requests

from api.GraphQL.data.test_data import url, variables_create_post
from api.GraphQL.queries.create_queries import create_post_query


def test_create_post():
    response=requests.post(url,json={"query":create_post_query,"variables": variables_create_post})
    data = response.json()
    post= data["data"]["createPost"]

    assert response.status_code == 200
    assert "id" in post
    assert post["title"]== "yuval"
    assert post["body"] == "trying graphql"
    print(data)