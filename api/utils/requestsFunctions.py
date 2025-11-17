import requests


def get_request(path):
    response = requests.get(path)
    return response


def post_request(headers, path, body):
    response = requests.post(url=path, json=body, headers=headers)
    return response


def put_request(headers, path, body):
    response = requests.put(url=path, json=body, headers=headers)
    return response


def delete_request(headers, path):
    response = requests.delete(url=path, headers=headers)
    return response
