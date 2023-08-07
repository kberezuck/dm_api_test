import allure

from dm_api_account.models import LoginCredentials


class Login:
    def __init__(self, facade):
        from services.dm_api_account import Facade
        self.facade: Facade = facade

    def set_headers(self, headers):
        self.facade.login_api.client.session.headers.update(headers)

    def login_user(self, login: str, password: str, remember_me: bool = True):
        response = self.facade.login_api.v1_account_login_post(
            _return_http_data_only=False,
            login_credentials=LoginCredentials(
                login=login,
                password=password,
                remember_me=remember_me
            )
        )
        return response

    def get_auth_token(self, login: str, password: str, remember_me: bool = True):
        with allure.step("Получение токена для хедеров"):
            response = self.login_user(login=login, password=password, remember_me=remember_me)
            x_dm_auth_token = str(response[2]['X-Dm-Auth-Token'])
        return x_dm_auth_token

    def logout_user(self, x_dm_auth_token: str, **kwargs):
        response = self.facade.login_api.v1_account_login_delete(
            _return_http_data_only=False,
            x_dm_auth_token=x_dm_auth_token,
            **kwargs
        )
        return response

    def logout_user_from_all_device(self, x_dm_auth_token: str, **kwargs):
        response = self.facade.login_api.v1_account_login_all_delete(
            _return_http_data_only=False,
            x_dm_auth_token=x_dm_auth_token,
            **kwargs
        )
        return response
