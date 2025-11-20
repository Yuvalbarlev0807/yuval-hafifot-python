import requests

from api.GraphQL.data.test_data import url
from api.GraphQL.queries.get_queries import get_post_by_id_query, get_user_by_id_query


def test_get_post_by_id():
 response = requests.post(url, json={"query": get_post_by_id_query})
 data = response.json()
 assert response.status_code == 200
 assert data["data"]["post"]["id"] == "2"
 print(data)

def test_get_user_by_id():
    response=requests.post(url,json={"query":get_user_by_id_query})
    data = response.json()
    assert response.status_code == 200
    assert data["data"]["user"]["id"] == "1"
    print(data)