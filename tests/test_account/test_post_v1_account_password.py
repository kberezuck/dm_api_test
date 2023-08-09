from datetime import datetime

import allure
from hamcrest import assert_that, has_properties, instance_of, starts_with

from dm_api_account.models import UserRole


@allure.suite("Тесты на проверку метода POST/v1/account/password")
@allure.sub_suite("Позитивные проверки")
class TestsPostV1AccountPassword:
    @allure.title("Сброс пароля")
    def test_post_v1_account_password(self, dm_api_facade, orm_db, prepare_user, assertions):
        """
        Тест на создание пользователя и сброс пароля
        """
        # Register new user
        login = prepare_user.login
        email = prepare_user.email
        password = prepare_user.password

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

        # Reset password
        response = dm_api_facade.account.reset_registered_user_password(
            login=login,
            email=email,
            x_dm_auth_token=x_dm_auth_token
        )
        print(response)

        # assert_that(response.resource, has_properties(
        #     {
        #         "login": login,
        #         "roles": [UserRole.guest, UserRole.player],
        #         "registration": instance_of(datetime)
        #     }
        # ))
        # assert_that(response.metadata["email"], starts_with("ks"))
