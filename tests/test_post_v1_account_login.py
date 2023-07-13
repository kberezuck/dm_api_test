import time
from datetime import datetime

import structlog
from hamcrest import assert_that, has_properties, instance_of

from dm_api_account.generic.helpers.mailhog import MailhogApi
from dm_api_account.models.login_credentials_model import LoginCredentials
from dm_api_account.models.user_envelope_model import UserRole
from services.dm_api_account import Facade

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account_login():
    mailhog = MailhogApi(host="http://localhost:5025")
    api = Facade(host="http://localhost:5051")

    # json = Registration(
    #     login="ksb30",
    #     email="ksb30@mail.ru",
    #     password="qwerty1234"
    # )
    #
    # response = api.account.post_v1_account(json=json)
    # assert response.status_code == 201, f"Ожидался статус код 201, а фактически {response.status_code}"
    time.sleep(2)
    token = mailhog.get_token_by_login(login=login)
    response = api.account.put_v1_account_token(token=token, status_code=200)

    json = LoginCredentials(
        login="ksb31",
        password="qwerty1234",
        rememberMe=True
    )

    response = api.login.post_v1_account_login(json=json)


    assert_that(response.resource, has_properties(
        {
            "login": "ksb31",
            "roles": [UserRole.guest, UserRole.player],
            "registration": instance_of(datetime)
        }
    ))


