import time

import allure


@allure.suite("Тесты на проверку метода PUT/v1/account/password")
@allure.sub_suite("Позитивные проверки")
class TestsPutV1AccountPassword:
    @allure.title("Установка нового пароля")
    def test_put_v1_account_password(self, dm_api_facade, orm_db, prepare_user, assertions):
        """
        Тест на установку нового пороля
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

        # Reset password
        dm_api_facade.account.reset_registered_user_password(
            login=login,
            email=email,
            x_dm_auth_token=x_dm_auth_token
        )
        time.sleep(2)
        # Change password
        new_password = 'qwerty1234'
        dm_api_facade.account.change_registered_user_password(
            login=login,
            old_password=password,
            new_password=new_password,
            x_dm_auth_token=x_dm_auth_token
        )
