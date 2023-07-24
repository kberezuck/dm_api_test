import random
from string import ascii_letters, digits

import pytest
from hamcrest import assert_that


def random_string(begin=1, end=30):
    simbols = ascii_letters + digits
    string = ''
    for _ in range(random.randint(begin, end)):
        string += random.choice(simbols)
    return string


# @pytest.mark.parametrize('login', [random_string() for _ in range(3)])
# @pytest.mark.parametrize('email', [random_string() + '@' + random_string() + '.ru' for _ in range(3)])
# @pytest.mark.parametrize('password', [random_string() for _ in range(3)])


@pytest.mark.parametrize('login, email, password, status_code, check', [
    ('12', '12@12.ru', '123456', 201, ''),                                  # Валидные данные
    ('12', '12@12.ru', random_string(1, 5), 400, {"Password": ["Short"]}),  # Пароль менее либо равен 5 символам
    ('1', '12@12.ru', '123456', 400, {"Login": ["Short"]}),                 # Логин менее 2 символов
    ('12', '12@', '123456', 400, {"Email": ["Invalid"]}),                   # Емейл не содержит доменную часть
    ('12', '12', '123456', 400, {"Email": ["Invalid"]})                     # Емейл не содержит символ @
])
def test_create_and_activated_user_with_random_params(
        dm_api_facade,
        orm_db,
        login,
        email,
        password,
        status_code,
        check
):
    orm_db.delete_user_by_login(login=login)
    dm_api_facade.mailhog.delete_all_messages()
    # Register new user
    response = dm_api_facade.account.register_new_user(
        login=login,
        email=email,
        password=password,
        status_code=status_code
    )
    if status_code == 201:

        dataset = orm_db.get_user_by_login(login=login)
        for row in dataset:
            assert_that(row.Login == login, row.Activated is False)

        orm_db.activate_user(login=login)

        dataset = orm_db.get_user_by_login(login=login)

        for row in dataset:
            assert_that(row.Activated is True)

        # Login user
        dm_api_facade.login.login_user(
            login=login,
            password=password,
            status_code=200
        )

    elif response.status_code == status_code:
        assert response.json()['errors'] == check,\
            f"Ожидаласть ошибка {check}, а фактически ошибка {response.json()['errors']}"
        return print(response.json()['errors'])
