import requests
from services.dm_api_account import DmApiAccount

def test_post_v1_account():
    api = DmApiAccount(host="http://localhost:5051")  # создали объект класса
    json = {                                          # переменная равна payload метода post_v1_account,
                                                      # которую мы вынесли в папку modules
        "login": "ksb3",
        "email": "ksb3@mail.ru",
        "password": "qwerty1234"
    }

    response = api.account.post_v1_account(
        json=json
    )

    print(response)
