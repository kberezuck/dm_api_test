import structlog
import time
from hamcrest import assert_that, has_properties
from dm_api_account.models.registration_model import Registration
from dm_api_account.models.user_envelope_model import UserRole, Rating
from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_token():
    mailhog = MailhogApi(host="http://localhost:5025")
    api = DmApiAccount(host="http://localhost:5051")

    # json = Registration(
    #     login="ksb31",
    #     email="ksb31@mail.ru",
    #     password="qwerty1234"
    # )
    #
    # response = api.account.post_v1_account(json=json)
    # time.sleep(2)

    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account_token(token=token, status_code=200)
    assert_that(response.resource, has_properties(
        {
            "login": "ksb31",
            "roles": [UserRole.guest, UserRole.player],
        }
    ))
