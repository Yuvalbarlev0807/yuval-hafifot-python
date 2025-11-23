import requests

from api.GraphQL.data.test_data import url, variables_delete_post
from api.GraphQL.queries.delete_queries import delete_post_query


def test_delete_post_by_id():
    response = requests.post(url, json={"query": delete_post_query, "variables": variables_delete_post})
    data = response.json()
    assert response.status_code == 200
    assert data["data"]["deletePost"] == True
    print(data)
