from collections import namedtuple
from pathlib import Path

import allure
import pytest
import structlog
from grpclib.client import Channel
from vyper import v

from apis.dm_api_search_async import SearchEngineStub
from data.post_v1_account import PostV1AccountData as user_data
from generic.assertions.check_user import AssertionsCheckUser
from generic.helpers.dm_db import DmDataBase
from generic.helpers.mailhog import MailhogApi
from generic.helpers.orm_db import OrmDataBase
from generic.helpers.search import Search
from services.dm_api_account import Facade

# делаем лог "красивым" и удобочитаемым
structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


@pytest.fixture()
def mailhog():
    return MailhogApi(host=v.get('service.mailhog'))


@pytest.fixture()
def dm_api_facade(mailhog):
    return Facade(
        host=v.get('service.dm_api_account'),
        mailhog=mailhog
    )


options = (
    'service.dm_api_account',
    'service.mailhog',
    'service.target',
    'service.host',
    'service.port',
    'database.dm3_5.host'
)


@pytest.fixture()
def dm_db():
    db = DmDataBase(
        user=v.get('database.dm3_5.user'),
        password=v.get('database.dm3_5.password'),
        host=v.get('database.dm3_5.host'),
        database=v.get('database.dm3_5.database')
    )
    return db


@pytest.fixture()
def orm_db():
    db = OrmDataBase(
        user=v.get('database.dm3_5.user'),
        password=v.get('database.dm3_5.password'),
        host=v.get('database.dm3_5.host'),
        database=v.get('database.dm3_5.database')
    )
    return db


@pytest.fixture()
def grpc_search():
    client = Search(target=v.get('service.target'))
    yield client
    client.close()


@pytest.fixture()
def grpc_search_async():
    channel = Channel(host=v.get('service.host'), port=v.get('service.port'))
    client = SearchEngineStub(channel)
    yield client
    channel.close()


@pytest.fixture()
def assertions(orm_db):
    return AssertionsCheckUser(orm_db)


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

@allure.step("Подготовка тестового пользователя")
@pytest.fixture
def prepare_user(dm_api_facade, orm_db):
    user = namedtuple('User', 'login, email, password')
    User = user(login=user_data.login, email=user_data.email, password=user_data.password)
    # удаления юзера перед началом теста, запрашиваем БД, чтобы убедиться, что такого юзера там нет
    orm_db.delete_user_by_login(login=User.login)
    dataset = orm_db.get_user_by_login(login=User.login)
    assert len(dataset) == 0
    dm_api_facade.mailhog.delete_all_messages()

    return User


@pytest.fixture(autouse=True)
def set_config(request):
    config = Path(__file__).parent.joinpath('config')
    config_name = request.config.getoption('--env')
    v.set_config_name(config_name)
    v.add_config_path(config)
    v.read_in_config()
    for option in options:
        v.set(option, request.config.getoption(f'--{option}'))


def pytest_addoption(parser):
    parser.addoption('--env', action='store', default='stg')
    for option in options:
        parser.addoption(f'--{option}', action='store', default=None)
