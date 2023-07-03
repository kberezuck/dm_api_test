from requests import Response

# from dm_api_account.models.bad_request_model import BadRequestModel
from dm_api_account.models.change_email_model import ChangeEmailModel
from dm_api_account.models.change_password_model import ChangePasswordModel
# from dm_api_account.models.general_error import GeneralError
from dm_api_account.models.registration_model import RegistrationModel
from dm_api_account.models.reset_password_model import ResetPasswordModel
from dm_api_account.models.user_details_envelope import UserDetailsEnvelope
from dm_api_account.models.user_envelope_model import UserEnvelopeModel
from restclient.restclient import Restclient


class AccountApi:

    def __init__(self, host, headers=None):
        self.host = host
        self.headers = headers
        self.client = Restclient(host=host, headers=headers)
        if headers:
            self.client.session.headers.update(headers)

    def get_v1_account(self, **kwargs):
        """
        Get current user
        :return:
        """

        response = self.client.get(
            path=f"/v1/account",  # переменная self.host не нужна, так как мы добавлеям этот хост в Restclient
            **kwargs
        )
        UserDetailsEnvelope(**response.json())
        return response

    def post_v1_account(self, json: RegistrationModel,
                        **kwargs) -> Response:  # -> значит, что этой функцией мы возвращаем объект Response
        """
        :param json registration_model
        Register new user
        :return:
        """
        response = self.client.post(
            path=f"/v1/account",
            json=json.model_dump(by_alias=True, exclude_none=True),
            # by_alias- использование только тех "названий переменных", кот-е мы указали.
            **kwargs  # exclude - выключает поля, кот-е ничем незаполнены (опциональные) если их нет, - мы и не поверяем
        )

        # BadRequestModel(**response.json())
        return response

    def post_v1_account_password(self, json: ResetPasswordModel, **kwargs) -> Response:
        """
        :param json reset_password_module
        Reset registered user password
        :return:
        """
        response = self.client.post(
            path=f"/v1/account/password",
            json=json.model_dump(by_alias=True, exclude_none=True),
            **kwargs
        )
        UserEnvelopeModel(**response.json())
        # BadRequestModel(**response.json())
        return response

    def put_v1_account_email(self, json: ChangeEmailModel, **kwargs) -> Response:
        """
        :param json change_email_model
        Change registered user email
        :return:
        """
        response = self.client.put(
            path=f"/v1/account/email",
            json=json.model_dump(by_alias=True, exclude_none=True),
            **kwargs
        )
        UserEnvelopeModel(**response.json())
        # BadRequestModel(**response.json())
        return response

    def put_v1_account_password(self, json: ChangePasswordModel, **kwargs) -> Response:
        """
        :param json change_password_model
        Change registered user password
        :return:
        """
        response = self.client.put(
            path=f"/v1/account/password",
            json=json.model_dump(by_alias=True, exclude_none=True),
            **kwargs
        )
        UserEnvelopeModel(**response.json())
        # BadRequestModel(**response.json())
        return response

    def put_v1_account_token(self, token, **kwargs):
        """
        Activate registered user
        :return:
        """
        response = self.client.put(
            path=f"/v1/account/{token}",
            **kwargs
        )
        UserEnvelopeModel(**response.json())
        # GeneralError(**response.json())
        return response
