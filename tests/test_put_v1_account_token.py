import allure
from hamcrest import assert_that, has_properties

from dm_api_account.models.user_envelope_model import UserRole


@allure.suite("Тесты на проверку метода PUT/v1/account/token")
@allure.sub_suite("Позитивные проверки")
class TestsPutV1AccountToken:
    @allure.title("Получение токена регистрации из письма")
    def test_put_v1_account_token(self, dm_api_facade, orm_db, prepare_user, assertions):
        """
        Тест на получение токена при создании пользователя
        """
        login = prepare_user.login
        email = prepare_user.email
        password = prepare_user.password
        dm_api_facade.account.register_new_user(
            login=login,
            email=email,
            password=password,
            status_code=201
        )
        assertions.check_user_was_created(login=login)
        token = dm_api_facade.mailhog.get_token_by_login(login=login, search='activate')
        response = dm_api_facade.account_api.put_v1_account_token(token=token, status_code=200)
        assert_that(response.resource, has_properties(
            {
                "login": login,
                "roles": [UserRole.guest, UserRole.player]
            }
        ))
