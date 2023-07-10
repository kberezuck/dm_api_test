from datetime import datetime

import structlog
from hamcrest import assert_that, has_properties, instance_of, contains_string, starts_with

from dm_api_account.models.reset_password_model import ResetPassword
from dm_api_account.models.user_envelope_model import UserRole
from services.dm_api_account import Facade

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account_password():
    api = Facade(host="http://localhost:5051")
    json = ResetPassword(
        login="ksb31",
        email="ksb31@mail.ru"
    )

    response = api.account.post_v1_account_password(
        json=json
    )
    assert_that(response.resource, has_properties(
        {
            "login": "ksb31",
            "roles": [UserRole.guest, UserRole.player],
        }
    ))
    assert_that(response.resource.registration, instance_of(datetime))
    assert_that(response.metadata["email"],  starts_with("ks"))
