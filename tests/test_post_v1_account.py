import structlog

from dm_api_account.models.registration_model import RegistrationModel
from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi

# делаем лог "красивым" и удобочитаемым
structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account():
    mailhog = MailhogApi(host="http://localhost:5025")
    api = DmApiAccount(host="http://localhost:5051")  # создали объект класса
    json = RegistrationModel(  # переменная равна payload метода post_v1_account,
        # которую мы вынесли в папку models
        login="ksb23",
        email="ksb23@mail.ru",
        password="qwerty1234"
    )

    response = api.account.post_v1_account(json=json)
    assert response.status_code == 201, f"Ожидался статус код 201, а фактически {response.status_code}"
    # token = mailhog.get_token_from_last_email()
    # response = api.account.put_v1_account_token(token=token)
