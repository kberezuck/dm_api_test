import requests

url = "http://localhost:5051/v1/account"


def post_v1_acount():
    payload = {
        "login": "<string>",
        "email": "<string>",
        "password": "<string>"
    }
    headers = {
        'X-Dm-Auth-Token': '<string>',
        'X-Dm-Bb-Render-Mode': '<string>',
        'Content-Type': 'application/json',
        'Accept': 'text/plain'
    }

    response = requests.request("POST", url, headers=headers, json=payload)
