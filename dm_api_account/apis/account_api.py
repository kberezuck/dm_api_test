import requests
from requests import Response
from ..modules import registration_model
from ..modules import reset_password_model
from ..modules import change_email_model
from ..modules import change_password_model
from requests import session


class AccountApi:

    def __init__(self, host, headers=None):
        self.host = host
        self.headers = headers
        self.session = session()
        if headers:
            self.session.headers.update(headers)

    def get_v1_account(self, **kwargs):
        """
        Get current user
        :return:
        """

        response = self.session.get(
            url=f"{self.host}/v1/account",
            **kwargs
        )
        return response

    def post_v1_account(self, json: registration_model,
                        **kwargs) -> Response:  # -> значит, что этой функцией мы возвращаем объект Response
        """
        :param json registration_model
        Register new user
        :return:
        """
        response = self.session.post(
            url=f"{self.host}/v1/account",
            json=json,
            **kwargs
        )
        return response

    def post_v1_account_password(self, json: reset_password_model, **kwargs) -> Response:
        """
        :param json reset_password_module
        Reset registered user password
        :return:
        """
        response = self.session.post(
            url=f"{self.host}/v1/account/password",
            json=json,
            **kwargs
        )
        return response

    def put_v1_account_email(self, json: change_email_model, **kwargs) -> Response:
        """
        :param json change_email_model
        Change registered user email
        :return:
        """
        response = self.session.put(
            url=f"{self.host}/v1/account/email",
            json=json,
            **kwargs
        )
        return response

    def put_v1_account_password(self, json: change_password_model, **kwargs) -> Response:
        """
        :param json change_password_model
        Change registered user password
        :return:
        """
        response = self.session.put(
            url=f"{self.host}/v1/account/password",
            json=json,
            **kwargs
        )
        return response

    def put_v1_account_token(self, **kwargs):
        """
        Activate registered user
        :return:
        """
        token = "349e49d3-407a-4d0b-a95e-5f111c37d390"
        response = self.session.put(
            url=f"{self.host}/v1/account/{token}",
            **kwargs
        )
        return response
