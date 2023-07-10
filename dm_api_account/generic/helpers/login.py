from model import LoginCredentials


class Login:

    def __init__(self, facade):
        from services.dm_api_account import Facade
        self.facade = Facade = facade

    def login_user(self, login: str, password: str, remember_me: bool = True):
        response = self.facade.login_api.post_v1_account_login(
            json=LoginCredentials(
                login=login,
                password=password,
                remember_me=remember_me

            )
        )
        return response
