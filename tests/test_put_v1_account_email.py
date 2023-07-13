from datetime import time

import structlog
from hamcrest import assert_that, has_properties

from dm_api_account.generic.helpers.mailhog import MailhogApi
from dm_api_account.models.change_email_model import ChangeEmail
from dm_api_account.models.registration_model import Registration
from dm_api_account.models.user_envelope_model import UserRole, Rating
from services.dm_api_account import Facade

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)

x = "@mail.ru"
login = "ksb50",
email = f"ksb50{x}",
password = "qwerty1234"


def test_put_v1_account_email():
    mailhog = MailhogApi(host="http://localhost:5025")
    api = Facade(host="http://localhost:5051")
    json = Registration(
        login=login,
        email=email,
        password=password
    )

    response = api.account.post_v1_account(json=json)
    time.sleep(2)
    token = mailhog.get_token_by_login(login=f'{login}')
    response = api.account.put_v1_account_token(token=token)

    json = ChangeEmail(
        login=login,
        email=email,
        password="qwerty1234"
    )
    response = api.account.put_v1_account_email(json=json)
    assert_that(response.resource, has_properties(
        {
            "login": "ksb50",
            "roles": [UserRole.guest, UserRole.player],
            "enabled": [Rating.Optional],
            "quality": [Rating.Optional],
            "quantity": [Rating.Optional],
        }
    ))
