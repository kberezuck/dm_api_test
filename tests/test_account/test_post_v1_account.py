import allure


@allure.suite("Тесты на проверку метода POST(host)/v1/account")
@allure.sub_suite("Позитивные проверки")
class TestsPostV1Account:
    @allure.title("Проверка регистрации и активации пользователя")
    def test_post_v1_account(self, dm_api_facade, orm_db, prepare_user, assertions):
        """
        Тест проверяет создание и активацию пользователя в базе данных
        """
        login = prepare_user.login
        email = prepare_user.email
        password = prepare_user.password

        response = dm_api_facade.account.register_new_user(
            login=login,
            email=email,
            password=password
        )

        assertions.check_user_was_created(login=login)
        orm_db.activate_user(login=login)
        assertions.check_user_was_activated(login=login)
        dm_api_facade.login.login_user(
            login=login,
            password=password
        )
