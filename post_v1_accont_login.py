import requests

url = "http://localhost:5051/v1/account/login"


def post_v1_account_login():
    payload = {
        "login": "<string>",
        "password": "<string>",
        "rememberMe": "<boolean>"
    }
    headers = {
        'X-Dm-Bb-Render-Mode': '<string>',
        'Content-Type': 'application/json',
        'Accept': 'text/plain'
    }

    response = requests.request("POST", url, headers=headers, json=payload)
