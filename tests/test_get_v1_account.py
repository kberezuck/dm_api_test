import structlog

from services.dm_api_account import Facade

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)

login = "ksb66"
email = "ksb66@mail.ru"
password = "qwerty1234"

def test_get_v1_account():
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

    # Get information
    api.account.get_current_user_info(headers=token)
