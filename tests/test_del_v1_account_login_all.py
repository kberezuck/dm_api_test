import requests

from services.dm_api_account import DmApiAccount

def test_del_v1_account_login_all():
    api = DmApiAccount(host="http://localhost:5051")

    response = api.login.del_v1_account_login_all()

    print(response)
