import structlog
from hamcrest import assert_that, has_properties

from dm_api_account.models.change_email_model import ChangeEmail
from dm_api_account.models.user_envelope_model import UserRole
from services.dm_api_account import Facade
from dm_api_account.generic.helpers.mailhog import MailhogApi

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_email():
    mailhog = MailhogApi(host="http://localhost:5025")
    api = Facade(host="http://localhost:5051")
    # json = RegistrationModel(
    #     login="ksb11",
    #     email="ksb11@mail.ru",
    #     password="qwerty1234"
    # )
    #
    # response = api.account.post_v1_account(json=json)
    # time.sleep(2)
    # token = mailhog.get_token_from_last_email()
    # response = api.account.put_v1_account_token(token=token)

    json = ChangeEmail(
        login="ksb31",
        email="ksbb31@mail.ru",
        password="qwerty1234"
    )
    response = api.account.put_v1_account_email(json=json)
    assert_that(response.resource, has_properties(
        {
            "login": "ksb31",
            "roles": [UserRole.guest, UserRole.player],
        }
    ))
