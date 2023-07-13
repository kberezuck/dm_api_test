import structlog
from hamcrest import assert_that, has_properties

from dm_api_account.generic.helpers.mailhog import MailhogApi
from dm_api_account.models.user_envelope_model import UserRole, Rating
from services.dm_api_account import Facade

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)

login = "ksb63"
email = "ksb63@mail.ru"
password = "qwerty1234"


def test_put_v1_account_token():
    mailhog = MailhogApi(host="http://localhost:5025")
    api = Facade(host="http://localhost:5051")

    # Register new user

    response = api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    # Get token from email
    token = api.mailhog.get_token_by_login(login=login)
    response = api.account_api.put_v1_account_token(token=token, status_code=200)
    assert_that(response.resource, has_properties(
        {
            "login": "ksb63",
            "roles": [UserRole.guest, UserRole.player],
            "enabled": [Rating.Optional],
            "quality": [Rating.Optional],
            "quantity": [Rating.Optional],
        }
    ))
