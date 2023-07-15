import structlog

from services.dm_api_account import Facade

# делаем лог "красивым" и удобочитаемым
structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)

login = "ksb65"
email = "ksb65@mail.ru"
password = "qwerty1234"

def test_post_v1_account():
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
