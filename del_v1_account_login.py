import requests

url = "http://localhost:5051/v1/account/login"


def del_v1_account_login():
    payload = {}
    headers = {
        'X-Dm-Auth-Token': '<string>',
        'X-Dm-Bb-Render-Mode': '<string>',
        'Accept': 'text/plain'
    }

    response = requests.request("DELETE", url, headers=headers, json=payload)
