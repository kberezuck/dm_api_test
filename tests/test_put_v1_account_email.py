from datetime import datetime

import structlog
from hamcrest import assert_that, has_properties, instance_of
from dm_api_account.models.user_envelope_model import UserRole, Rating
from services.dm_api_account import Facade

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)

login = "ksb91"
email = "ksb91@mail.ru"
password = "qwerty1234"


def test_put_v1_account_email():
    api = Facade(host="http://localhost:5051")

    # Register new user
    api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )

    # Register activate_user
    api.account.activate_registered_user(login=login)

    # Login user
    api.login.login_user(
        login=login,
        password=password
    )

    # Get authorisation token and set headers
    token = api.login.get_auth_token(login=login, password=password)
    api.account.set_headers(headers=token)

    new_email = 'ksbb91@mail.ru'
    response = api.account.change_email(
        login=login,
        email=new_email,
        password=password
    )

    assert_that(response.resource, has_properties(
        {
            "login": "ksb91",
            "roles": [UserRole.guest, UserRole.player],
            'online': instance_of(datetime)
        }
    ))
