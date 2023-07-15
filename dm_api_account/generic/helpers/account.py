from dm_api_account.models import ChangeEmail
from dm_api_account.models import ChangePassword
from dm_api_account.models import Registration
from dm_api_account.models import ResetPassword


# from dm_api_account.generic.helpers.mailhog import MailhogApi


class Account:
    def __init__(self, facade):
        from services.dm_api_account import Facade
        self.facade: Facade = facade

    def set_headers(self, headers):
        self.facade.account_api.client.session.headers.update(headers)

    def register_new_user(self, login: str, email: str, password: str):
        response = self.facade.account_api.post_v1_account(
            json=Registration(
                login=login,
                email=email,
                password=password
            )
        )
        return response

    def activate_registered_user(self, login: str):
        token = self.facade.mailhog.get_token_by_login(login=login)
        response = self.facade.account_api.put_v1_account_token(
            token=token,
            status_code=200
        )
        return response

    def get_current_user_info(self, **kwargs):
        response = self.facade.account_api.get_v1_account(**kwargs)
        return response

    def reset_registered_user_password(self, login: str, email: str, **kwargs):
        response = self.facade.account_api.post_v1_account_password(
            json=ResetPassword(
                login=login,
                email=email
            ))
        return response

    def change_registered_user_password(self, login: str, new_password: str, old_password: str, **kwargs):
        response = self.facade.account_api.put_v1_account_password(
            json=ChangePassword(
                login=login,
                token=self.facade.mailhog.get_token_by_reset_password(login=login),
                oldPassword=old_password,
                newPassword=new_password
            ))
        return response

    def change_email(self, login: str, email: str, password: str):
        response = self.facade.account_api.put_v1_account_email(
            json=ChangeEmail(
                login=login,
                email=email,
                password=password
            )
        )
        return response
