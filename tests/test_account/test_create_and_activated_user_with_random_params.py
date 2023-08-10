import random
from string import ascii_letters, digits

import allure
import pytest


def random_string(begin=1, end=30):
    simbols = ascii_letters + digits
    string = ''
    for _ in range(random.randint(begin, end)):
        string += random.choice(simbols)
    return string


@allure.suite("Тесты на проверку метода POST(host)/v1/account по рандомным параметрам")
@allure.sub_suite("Позитивные проверки")
class TestsPostV1Account:
    random_email = f'{random_string()}@{random_string()}.{random_string()}'
    valid_login = random_string(2)
    invalid_login = random_string(1, 1)
    valid_password = random_string(6)
    invalid_password = random_string(1, 5)
    invalid_email = f'{random_string(6)}'
    invalid_email_2 = random_string(1, 2).replace('@', '')

    random_data = [
        (valid_login, random_email, valid_password, 201, ''),
        (valid_login, random_email, invalid_password, 400, {"Password": ["Short"]}),
        (invalid_login, random_email, valid_password, 400, {"Login": ["Short"]}),
        (valid_login, invalid_email, valid_password, 400, {"Email": ["Invalid"]}),
        (valid_login, invalid_email_2, valid_password, 400, {"Email": ["Invalid"]})
    ]

    @pytest.mark.parametrize('login, email, password, status_code, check', random_data)
    @allure.title("Создание пользователя по рандомным параметрам и его активация")
    def test_create_and_activated_user_with_random_params(self,
                                                          dm_api_facade,
                                                          orm_db,
                                                          assertions,
                                                          email,
                                                          login,
                                                          password,
                                                          status_code,
                                                          check
                                                          ):
        """
        Тест на создание и активацию пользователя при рандомных параметрах
        :param dm_api_facade:
        :param orm_db:          Обращение к базе данных
        :param assertions:      Проверки по полям базы данных
        :param email:           Е-мэил
        :param login:           Логин
        :param password:        Пароль
        :param status_code:     Предполагаемый статус код
        :param check:           Расшифровка ошибки
        :return:
        """
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

            assertions.check_user_was_created(login=login)
            orm_db.activate_user(login=login)
            assertions.check_user_was_activated(login=login)

            # Login user
            dm_api_facade.login.login_user(
                login=login,
                password=password,
                status_code=200
            )

        elif response.status_code == status_code:
            assert response.json()['errors'] == check, \
                f"Ожидаласть ошибка {check}, а фактически ошибка {response.json()['errors']}"
