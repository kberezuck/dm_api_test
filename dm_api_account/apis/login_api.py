from __future__ import annotations

from requests import Response

from restclient.restclient import Restclient
from ..models import *
from ..utilities import validate_request_json, validate_status_code


class LoginApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.headers = headers
        self.client = Restclient(host=host, headers=headers)
        if headers:
            self.client.session.headers.update(headers)

    def post_v1_account_login(
            self,
            json: LoginCredentials,
            status_code: int = 200
    ) -> Response:
        """
        Authenticate via credentials
        :param status_code:
        :param json: login_credentials_model
        :return:
        """

        response = self.client.post(
            path=f"/v1/account/login",
            json=validate_request_json(json)
        )
        validate_status_code(response, status_code)
        if response.status_code == 200:
            UserEnvelope(**response.json())
        return response

        # BadRequestModel(**response.json())
        # GeneralError(**response.json())

    def del_v1_account_login(
            self,
            status_code: int = 204,
            **kwargs
    ) -> Response:
        """
        :param status_code:
        Logout as current user
        :return:
        """
        response = self.client.delete(
            path=f"/v1/account/login",
            **kwargs
        )
        validate_status_code(response, status_code)
        return response
        # GeneralError(**response.json())

    def delete_v1_account_login_all(
            self,
            status_code: int = 204,
            **kwargs
    ) -> Response:
        """
        :param status_code:
        Logout from every device
        :return:
        """
        response = self.client.delete(
            path=f"/v1/account/login/all",
            **kwargs
        )
        validate_status_code(response, status_code)
        return response
        # GeneralError(**response.json())
