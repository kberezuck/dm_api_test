from collections import namedtuple

import pytest
import structlog

from generic.helpers.dm_db import DmDataBase
from generic.helpers.mailhog import MailhogApi
from generic.helpers.orm_db import OrmDataBase
from services.dm_api_account import Facade

# делаем лог "красивым" и удобочитаемым
structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


@pytest.fixture()
def mailhog():
    return MailhogApi(host="http://localhost:5025")


@pytest.fixture()
def dm_api_facade(mailhog, request):
    host = request.config.getoption('--env')
    return Facade(host=host, mailhog=mailhog)


@pytest.fixture()
def dm_db():
    db = DmDataBase(user='postgres', password='admin', host='localhost', database='dm3.5')
    return db


@pytest.fixture()
def orm_db():
    db = OrmDataBase(user='postgres', password='admin', host='localhost', database='dm3.5')
    return db


# @pytest.fixture
# def prepare_user(dm_api_facade, dm_db):
#     user = namedtuple('User', 'login, email, password')
#     User = user(login='ksb022', email='ksb022@mail.ru', password='qwert1234')
#     # удаления юзера перед началом теста, запрашиваем БД, чтобы убедиться, что такого юзера там нет
#     dm_db.delete_user_by_login(login=User.login)
#     dataset = dm_db.get_user_by_login(login=User.login)
#     assert len(dataset) == 0
#     dm_api_facade.mailhog.delete_all_messages()
#
#     return User

@pytest.fixture
def prepare_user(dm_api_facade, orm_db):
    user = namedtuple('User', 'login, email, password')
    User = user(login='ksb24', email='ksb024@mail.ru', password='qwerty1234')
    # удаления юзера перед началом теста, запрашиваем БД, чтобы убедиться, что такого юзера там нет
    orm_db.delete_user_by_login(login=User.login)
    dataset = orm_db.get_user_by_login(login=User.login)
    assert len(dataset) == 0
    dm_api_facade.mailhog.delete_all_messages()

    return User


def pytest_addoption(parser):
    parser.addoption('--env', action='store', default='http://localhost:5051')
