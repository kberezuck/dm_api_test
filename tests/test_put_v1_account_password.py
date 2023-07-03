import structlog

from dm_api_account.models.change_password_model import ChangePasswordModel
from services.dm_api_account import DmApiAccount

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_password():
    api = DmApiAccount(host="http://localhost:5051")
    json = ChangePasswordModel(
        login="ksb23",
        token="9a1adcfd-88f5-41c2-a190-484438ba7e2d",
        oldPassword="qwerty1234",
        newPassword="1234qwerty"
    )

    response = api.account.put_v1_account_password(
        json=json
    )
