import structlog

from dm_api_account.models.reset_password_model import ResetPasswordModel
from services.dm_api_account import DmApiAccount

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account_password():
    api = DmApiAccount(host="http://localhost:5051")
    json = ResetPasswordModel(
        login="ksb23",
        email="ksbb23@mail.ru"
    )

    response = api.account.post_v1_account_password(
        json=json
    )
