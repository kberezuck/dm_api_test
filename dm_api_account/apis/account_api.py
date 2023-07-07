from __future__ import annotations

from requests import Response

from restclient.restclient import Restclient
from ..models import *
from ..utilities import validate_request_json, validate_status_code


class AccountApi:

    def __init__(self, host, headers=None):
        self.host = host
        self.headers = headers
        self.client = Restclient(host=host, headers=headers)
        if headers:
            self.client.session.headers.update(headers)

    def get_v1_account(
            self,
            status_code: int = 200,
            **kwargs
    ) -> Response | UserDetailsEnvelope:
        """
        :param status_code:
        Get current user
        :return:
        """

        response = self.client.get(  # переменная self.host не нужна, так как мы добавлеям этот хост в Restclient
            path=f"/v1/account",
            **kwargs
        )
        validate_status_code(response, status_code)
        if response.status_code == 200:
            return UserDetailsEnvelope(**response.json())
        return response

    def post_v1_account(
            self,
            json: Registration,
            status_code: int = 201,
            **kwargs
    ) -> Response:  # -> значит, что этой функцией мы возвращаем объект Response
        """
        :param status_code:
        :param json registration_model
        Register new user
        :return:
        """
        response = self.client.post(
            path=f"/v1/account",
            json=validate_request_json(json),
            # by_alias- использование только тех "названий переменных", кот-е мы указали.
            **kwargs  # exclude - выключает поля, кот-е ничем незаполнены (опциональные) если их нет, - мы и не поверяем
        )
        validate_status_code(response, status_code)
        return response
        # BadRequestModel(**response.json())


    def post_v1_account_password(
            self,
            json: ResetPassword,
            status_code: int = 200,
            **kwargs
    ) -> Response | UserEnvelope:

        """
        :param status_code:
        :param json reset_password_module
        Reset registered user password
        :return:
        """
        response = self.client.post(
            path=f"/v1/account/password",
            json=validate_request_json(json),
            **kwargs
        )
        validate_status_code(response, status_code)
        if response.status_code == 200:
            return UserEnvelope(**response.json())
        return response

        # BadRequestModel(**response.json())


    def put_v1_account_email(
            self,
            json: ChangeEmail,
            status_code: int = 200,
            **kwargs
    ) -> Response | UserEnvelope:
        """
        :param status_code:
        :param json change_email_model
        Change registered user email
        :return:
        """
        response = self.client.put(
            path=f"/v1/account/email",
            json=validate_request_json(json),
            **kwargs
        )
        validate_status_code(response, status_code)
        if response.status_code == 200:
            return UserEnvelope(**response.json())
        return response
        # BadRequestModel(**response.json())


    def put_v1_account_password(
            self,
            json: ChangePassword,
            status_code: int = 200,
            **kwargs
    ) -> Response | UserEnvelope:
        """
        :param status_code:
        :param json change_password_model
        Change registered user password
        :return:
        """
        response = self.client.put(
            path=f"/v1/account/password",
            json=validate_request_json(json),
            **kwargs
        )
        validate_status_code(response, status_code)
        if response.status_code == 200:
            return UserEnvelope(**response.json())
        return response
        # BadRequestModel(**response.json())


    def put_v1_account_token(
            self,
            token: str,
            status_code: int == 200,
            **kwargs
    ) -> Response | UserEnvelope:
        """
        :param token:
        :param status_code:
        Activate registered user
        :return:
        """
        response = self.client.put(
            path=f"/v1/account/{token}",
            **kwargs
        )
        validate_status_code(response, status_code)
        if response.status_code == 200:
            return UserEnvelope(**response.json())
        return response
        # GeneralError(**response.json())
