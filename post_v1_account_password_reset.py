import requests

url = "http://localhost:5051/v1/account/password"


def post_v1_account_password_reset():
    payload = {
        "login": "<string>",
        "email": "<string>"
    }
    headers = {
        'X-Dm-Auth-Token': '<string>',
        'X-Dm-Bb-Render-Mode': '<string>',
        'Content-Type': 'application/json',
        'Accept': 'text/plain'
    }

    response = requests.request("POST", url, headers=headers, json=payload)
