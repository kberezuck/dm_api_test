import structlog

from dm_api_account.models.Authenticate_credentials_model import AuthenticateCredentialsModel
from dm_api_account.models.registration_model import RegistrationModel
from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account_login():
    mailhog = MailhogApi(host="http://localhost:5025")
    api = DmApiAccount(host="http://localhost:5051")

    json = RegistrationModel(
        login="ksb12",
        email="ksb12@mail.ru",
        password="qwerty1234"
    )

    response = api.account.post_v1_account(json=json)
    assert response.status_code == 201, f"Ожидался статус код 201, а фактически {response.status_code}"
    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account_token(token=token)

    json = AuthenticateCredentialsModel(
        login="ksb12",
        password="qwerty1234",
        rememberMe=True
    )

    response = api.login.post_v1_account_login(json=json)
