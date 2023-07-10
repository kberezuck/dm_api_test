from services.dm_api_account import Facade


def test_del_v1_account_login():
    api = Facade(host="http://localhost:5051")

    response = api.login.del_v1_account_login()

    print(response)
