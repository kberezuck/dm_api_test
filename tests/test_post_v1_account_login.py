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


login = "ksb67"
email = "ksb67@mail.ru"
password = "qwerty1234"

def test_post_v1_account_login():
    mailhog = MailhogApi(host="http://localhost:5025")
    api = Facade(host="http://localhost:5051")

    # Register new user
    response = api.account.register_new_user(
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

    # Reset password
    api.account.reset_registered_user_password(login=login, email=email)
