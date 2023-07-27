import allure


@allure.suite("Тесты на проверку метода DEL/v1/account/login")
@allure.sub_suite("Позитивные проверки")
class TestsDelV1AccountLogin:
    @allure.title("Выход из текущего аккаунта")
    def test_del_v1_account_login(self, dm_api_facade, orm_db, prepare_user, assertions):
        """
        Тест на все + разлогирование из аккаунта
        """
        login = prepare_user.login
        email = prepare_user.email
        password = prepare_user.password

        # Register new user

        response = dm_api_facade.account.register_new_user(
            login=login,
            email=email,
            password=password,
            status_code=201
        )

        assertions.check_user_was_created(login=login)
        orm_db.activate_user(login=login)
        assertions.check_user_was_activated(login=login)

        # Login user
        dm_api_facade.login.login_user(
            login=login,
            password=password,
            status_code=200
        )

        # Get authorisation token and set headers
        token = dm_api_facade.login.get_auth_token(
            login=login,
            password=password,
            status_code=200
        )
        dm_api_facade.login.set_headers(headers=token)

        # Logout
        dm_api_facade.login.logout_user(status_code=204)
