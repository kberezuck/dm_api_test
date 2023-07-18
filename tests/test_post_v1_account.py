import time

import structlog

from dm_api_account.generic.helpers.db import DmDataBase
from services.dm_api_account import Facade

# делаем лог "красивым" и удобочитаемым
structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)

login = "ksb016"
email = "ksb016@mail.ru"
password = "qwerty1234"


def test_post_v1_account():
    api = Facade(host="http://localhost:5051")

    db = DmDataBase(user='postgres', password='admin', host='localhost', database='dm3.5')

    # удаления юзера перед началом теста, запрашиваем БД, чтобы убедиться, что такого юзера там нет
    db.delete_user_by_login(login=login)
    dataset = db.get_user_by_login(login=login)
    assert len(dataset) == 0

    api.mailhog.delete_all_messages()

    # Register new user
    response = api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )

    # получение юзера по логину, для проверки наличия записи в БД

    dataset = db.get_user_by_login(login=login)
    for row in dataset:
        assert row['Login'] == login, f"User {login} is not registered"
        assert row['Activated'] is False, f"User {login} was activated"

    # Register activate_user
    api.account.activate_registered_user(login=login)
    time.sleep(2)

    dataset = db.get_user_by_login(
        login=login)  # перезапрашиваем данные из БЗ, чтобы прочекать внесенные в ней изменения

    # проверка, что юзер активирован
    for row in dataset:
        assert row['Activated'] is True, f"User {login} is not activated"

    # Login user
    api.login.login_user(
        login=login,
        password=password
    )
