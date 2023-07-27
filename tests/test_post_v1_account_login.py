import allure


@allure.suite("Тесты на проверку метода POST/v1/account/login")
@allure.sub_suite("Позитивные проверки")
class TestsPostV1AccountLogin:
    @allure.title("Создание пользователя и вход в аккаунт")
    def test_post_v1_account_login(self, dm_api_facade, orm_db, prepare_user, assertions):
        """
        Тест на создание пользователя и вход в аккаунт
        """
        login = prepare_user.login
        email = prepare_user.email
        password = prepare_user.password

        # Register new user
        dm_api_facade.account.register_new_user(
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
