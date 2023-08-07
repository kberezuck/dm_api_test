from dm_api_account.models import ChangeEmail
from dm_api_account.models import ChangePassword
from dm_api_account.models import Registration
from dm_api_account.models import ResetPassword


class Account:
    def __init__(self, facade):
        from services.dm_api_account import Facade
        self.facade: Facade = facade

    # def set_headers(self, api_client):
    #     self.facade.account_api.api_client.default_headers(api_client)

    def register_new_user(self, login: str, email: str, password: str):
        response = self.facade.account_api.register(
            _return_http_data_only=False,
            registration=Registration(
                login=login,
                email=email,
                password=password
            )
        )
        return response

    def activate_registered_user(self, login: str):
        token = self.facade.mailhog.get_token_by_login(login=login, search='activate')
        response = self.facade.account_api.activate(
            _return_http_data_only=False,
            token=token
        )
        return response

    def get_current_user_info(self, x_dm_auth_token: str, **kwargs):
        response = self.facade.account_api.get_current(
            _return_http_data_only=False,
            x_dm_auth_token=x_dm_auth_token,
            **kwargs)
        return response

    def reset_registered_user_password(self, login: str, email: str, x_dm_auth_token: str):
        response = self.facade.account_api.reset_password(
            _return_http_data_only=False,
            reset_password=ResetPassword(
                login=login,
                email=email
            ),
            x_dm_auth_token=x_dm_auth_token

        )
        return response

    def change_registered_user_password(self, login: str, new_password: str, old_password: str, x_dm_auth_token: str):
        token = self.facade.mailhog.get_token_by_login(login=login, search='password')
        response = self.facade.account_api.change_password(
            _return_http_data_only=False,
            change_password=ChangePassword(
                login=login,
                token=token,
                old_password=old_password,
                new_password=new_password
            ),
            x_dm_auth_token=x_dm_auth_token
        )
        return response

    def change_email(self, login: str, email: str, password: str, x_dm_auth_token: str):
        response = self.facade.account_api.change_email(
            _return_http_data_only=False,
            change_email=ChangeEmail(
                login=login,
                email=email,
                password=password
            ),
            x_dm_auth_token=x_dm_auth_token
        )
        return response
