import requests
from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)

def test_put_v1_account_token():
    mailhog = MailhogApi(host="http://localhost:5025")
    api = DmApiAccount(host="http://localhost:5051")

    json = {
        "login": "ksb10",
        "email": "ksb10@mail.ru",
        "password": "qwerty1234"
    }

    response = api.account.post_v1_account(json=json)
    assert response.status_code == 201, f"Ожидался статус код 201, а фактически {response.status_code}"
    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account_token(token=token)

