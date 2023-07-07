import structlog

from dm_api_account.models.change_password_model import ChangePassword
from services.dm_api_account import DmApiAccount

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_password():
    api = DmApiAccount(host="http://localhost:5051")
    json = ChangePassword(
        login="ksb31",
        token="a3866292-5193-439d-8318-517f00c993f8",
        oldPassword="qwerty1234",
        newPassword="1234qwerty"
    )

    response = api.account.put_v1_account_password(
        json=json
    )
