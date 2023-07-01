from dm_api_account.models.reset_password_model import ResetPasswordModel
from services.dm_api_account import DmApiAccount


def test_post_v1_account_password():
    api = DmApiAccount(host="http://localhost:5051")
    json = ResetPasswordModel(
        login="ksb3",
        email="ksb3@mail.ru"
    )

    response = api.account.post_v1_account_password(
        json=json
    )

    print(response)
    print(response.json())
