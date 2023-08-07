import allure


@allure.suite("Тесты на проверку метода GET/v1/account")
@allure.sub_suite("Позитивные проверки")
class TestsGetV1Account:
    @allure.title("Получение информации авторизированного пользователя")
    def test_get_v1_account(self, dm_api_facade, orm_db, prepare_user, assertions):
        """
        Тест на все + получение информации пользователя
        """
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

        # dm_api_facade.account.set_headers(x_dm_auth_token=x_dm_auth_token)

        # Get information
        dm_api_facade.account.get_current_user_info(x_dm_auth_token=x_dm_auth_token)
