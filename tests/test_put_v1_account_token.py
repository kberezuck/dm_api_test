import requests
from services.dm_api_account import DmApiAccount

def test_put_v1_account_token():

    api = DmApiAccount(host="http://localhost:5051")
    
    token="123456789"
    response = api.account.put_v1_account_token(token)

    print(response)