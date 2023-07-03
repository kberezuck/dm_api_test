from requests import Response

from dm_api_account.models.Authenticate_credentials_model import AuthenticateCredentialsModel
# from dm_api_account.models.bad_request_model import BadRequestModel
# from dm_api_account.models.general_error import GeneralError
from dm_api_account.models.user_envelope_model import UserEnvelopeModel
from restclient.restclient import Restclient


class LoginApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.headers = headers
        self.client = Restclient(host=host, headers=headers)
        if headers:
            self.client.session.headers.update(headers)

    def post_v1_account_login(self, json: AuthenticateCredentialsModel) -> Response:
        """
        :param json Authenticate_credentials_model
        Authenticate via credentials
        :return:
        """

        response = self.client.post(
            path=f"/v1/account/login",
            json=json.model_dump(by_alias=True, exclude_none=True)
        )
        UserEnvelopeModel(**response.json())
        # BadRequestModel(**response.json())
        # GeneralError(**response.json())
        return response

    def del_v1_account_login(self, **kwargs) -> Response:
        """
        Logout as current user
        :return:
        """
        response = self.client.delete(
            path=f"/v1/account/login",
            **kwargs
        )
        # GeneralError(**response.json())
        return response

    def v1_account_login_all(self, **kwargs) -> Response:
        """
        Logout from every device
        :return:
        """
        response = self.client.delete(
            path=f"/v1/account/login/all",
            **kwargs
        )
        # GeneralError(**response.json())
        return response
