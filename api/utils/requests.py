import requests


def get_request(path):
    response = requests.get(path)
    return response

