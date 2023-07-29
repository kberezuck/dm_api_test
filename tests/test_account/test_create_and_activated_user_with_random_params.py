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
    @pytest.mark.parametrize('login, email, password, status_code, check', [
        ('12', '12@12.ru', '123456', 201, ''),  # Валидные данные
        ('12', '12@12.ru', random_string(1, 5), 400, {"Password": ["Short"]}),  # Пароль менее либо равен 5 символам
        ('1', '12@12.ru', '123456', 400, {"Login": ["Short"]}),  # Логин менее 2 символов
        ('12', '12@', '123456', 400, {"Email": ["Invalid"]}),  # Емейл не содержит доменную часть
        ('12', '12', '123456', 400, {"Email": ["Invalid"]})  # Емейл не содержит символ @
    ])
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
