import requests
from services.dm_api_account import DmApiAccount


def test_put_v1_account_password():
    api = DmApiAccount(host="http://localhost:5051")
    json = {
        "login": "ksb3",
        "token": "814c4671-4a52-46a0-aaaa-f00c68f04b27",
        "oldPassword": "qwerty1234",
        "newPassword": "1234qwerty"
    }

    response = api.account.put_v1_account_password(
        json=json
    )

    print(response)
    print(response.json())
