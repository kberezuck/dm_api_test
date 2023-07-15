from services.dm_api_account import Facade

login = "ksb65"
email = "ksb65@mail.ru"
password = "qwerty1234"


def test_del_v1_account_login():
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
    api.login.set_headers(headers=token)

    # Logout
    api.login.logout_user()
