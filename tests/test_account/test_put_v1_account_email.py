from datetime import datetime

import allure
from hamcrest import assert_that, has_properties, instance_of

from dm_api_account.models import UserRole


@allure.suite("Тесты на проверку метода PUT/v1/account/email")
@allure.sub_suite("Позитивные проверки")
class TestsPutV1AccountEmail:
    @allure.title("Установка нового е-мэйла")
    def test_put_v1_account_email(self, dm_api_facade, orm_db, prepare_user, assertions):
        """
        Тест на установку нового е-мэйла
        """
        login = prepare_user.login
        email = prepare_user.email
        password = prepare_user.password

        # Register new user
        dm_api_facade.account.register_new_user(
            login=login,
            email=email,
            password=password
        )

        assertions.check_user_was_created(login=login)
        orm_db.activate_user(login=login)
        assertions.check_user_was_activated(login=login)

        # Login user
        dm_api_facade.login.login_user(
            login=login,
            password=password
        )

        # Get authorisation token and set headers
        x_dm_auth_token = dm_api_facade.login.get_auth_token(
            login=login,
            password=password
        )
        # dm_api_facade.account.set_headers(headers=token)

        new_email = 'ksbb023@mail.ru'
        response = dm_api_facade.account.change_email(
            login=login,
            email=new_email,
            password=password,
            x_dm_auth_token=x_dm_auth_token
        )

        assert_that(response.resource, has_properties(
            {
                "login": "ksb24",
                "roles": [UserRole('Guest'), UserRole('Player')],
                'online': instance_of(datetime)
            }
        ))
