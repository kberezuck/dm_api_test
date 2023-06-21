import requests

url = "http://localhost:5051/v1/account"


def get_v1_account():
    payload = {}
    headers = {
        'X-Dm-Auth-Token': '<string>',
        'X-Dm-Bb-Render-Mode': '<string>',
        'Accept': 'text/plain'
    }

    response = requests.request("GET", url, headers=headers, json=payload)
