import requests

url = "http://localhost:5051/v1/account/<uuid>"


def put_v1_account_token():
    payload = {}
    headers = {
        'X-Dm-Auth-Token': '<string>',
        'X-Dm-Bb-Render-Mode': '<string>',
        'Accept': 'text/plain'
    }
    response = requests.request("PUT", url, headers=headers, json=payload)
