import requests
from requests import Response
from ..modules import Authenticate_credentials_model
from requests import session


class LoginApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.headers = headers
        self.session = session()
        if headers:
            self.session.headers.update(headers)

    def post_v1_account_login(self, json: Authenticate_credentials_model) -> Response:
        """
        :param json Authenticate_credentials_model
        Authenticate via credentials
        :return:
        """

        response = self.session.post(
            url=f"{self.host}/v1/account/login",
            json=json
        )
        return response

    def del_v1_account_login(self, **kwargs) -> Response:
        """
        Logout as current user
        :return:
        """
        response = self.session.delete(
            url=f"{self.host}/v1/account/login",
            **kwargs
        )

        return response

    def v1_account_login_all(self, **kwargs) -> Response:
        """
        Logout from every device
        :return:
        """
        response = self.session.delete(
            url=f"{self.host}/v1/account/login/all",
            **kwargs
        )
        return response
