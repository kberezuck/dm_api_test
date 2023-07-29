from apis.dm_api_account.models import ChangeEmail
from apis.dm_api_account.models import ChangePassword
from apis.dm_api_account.models import Registration
from apis.dm_api_account.models import ResetPassword


class Account:
    def __init__(self, facade):
        from services.dm_api_account import Facade
        self.facade: Facade = facade

    def set_headers(self, headers):
        self.facade.account_api.client.session.headers.update(headers)

    def register_new_user(self, login: str, email: str, password: str, status_code: int):
        response = self.facade.account_api.post_v1_account(
            json=Registration(
                login=login,
                email=email,
                password=password
            ),
            status_code=status_code
        )
        return response

    def activate_registered_user(self, login: str, status_code: int):
        token = self.facade.mailhog.get_token_by_login(login=login, search='activate')
        response = self.facade.account_api.put_v1_account_token(
            token=token,
            status_code=status_code
        )
        return response

    def get_current_user_info(self, **kwargs):
        response = self.facade.account_api.get_v1_account(**kwargs)
        return response

    def reset_registered_user_password(self, login: str, email: str, status_code: int):
        response = self.facade.account_api.post_v1_account_password(
            json=ResetPassword(
                login=login,
                email=email
            ),
            status_code=status_code
        )
        return response

    def change_registered_user_password(self, login: str, new_password: str, old_password: str, status_code: int):
        token = self.facade.mailhog.get_token_by_login(login=login, search='password')
        response = self.facade.account_api.put_v1_account_password(
            json=ChangePassword(
                login=login,
                token=token,
                oldPassword=old_password,
                newPassword=new_password
            ),
            status_code=status_code
        )
        return response

    def change_email(self, login: str, email: str, password: str, status_code: int):
        response = self.facade.account_api.put_v1_account_email(
            json=ChangeEmail(
                login=login,
                email=email,
                password=password
            ),
            status_code=status_code
        )
        return response
