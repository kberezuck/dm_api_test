import structlog

from services.dm_api_account import Facade

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)

login = "ksb82"
email = "ksb82@mail.ru"
password = "1234qwerty"


def test_put_v1_account_password():
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

    # Change password
    new_password = 'qwerty1234'
    api.account.change_registered_user_password(
        login=login,
        old_password=password,
        new_password=new_password,
        token=token)
