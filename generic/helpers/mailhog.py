import json
import time

import allure
import requests
import structlog
from requests import Response
from restclient.restclient import Restclient

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def allure_attach(fn):
    def wrapper(*args, **kwargs):
        body = kwargs.get('json')
        if body:
            allure.attach(
                json.dumps(kwargs.get('json'), indent=2),
                name='request',
                attachment_type=allure.attachment_type.JSON
            )

        response = fn(*args, **kwargs)
        try:
            response_json = response.json()
        except requests.exceptions.JSONDecodeError:
            response_text = response.text
            status_code = f'<status_code {response.status_code}>'
            allure.attach(
                response_text if len(response_text) > 0 else status_code,
                name='response',
                attachment_type=allure.attachment_type.TEXT
            )
        else:
            allure.attach(
                json.dumps(response_json, indent=2),
                name='response',
                attachment_type=allure.attachment_type.JSON
            )
        return response

    return wrapper


class MailhogApi:
    def __init__(self, host="http://localhost:5025"):
        self.host = host
        self.client = Restclient(host=host)

    @allure_attach
    def get_api_v2_messages(self, limit: int = 50) -> Response:
        """
        Get message by limit
        :param limit:
        :return:
        """
        response = self.client.get(
            path=f"/api/v2/messages",
            params={
                "limit": limit
            }
        )
        return response

    def get_token_by_login(self, login: str, search: str, attempt=50):
        """
        Get user activation token from email by login
        :return:
        """
        with allure.step("Получение токена из письма"):
            if attempt == 0:
                raise AssertionError(f'Не удалось получить письмо с логином {login}')
        emails = self.get_api_v2_messages(limit=5).json()["items"]
        for email in emails:
            user_data = json.loads(email['Content']["Body"])
            if login == user_data.get("Login") and search == 'activate':
                token = user_data['ConfirmationLinkUrl'].split('/')[-1]
                print(token)
                return token
            elif login == user_data.get("Login") and search == 'password':
                token = user_data['ConfirmationLinkUri'].split('/')[-1]
                print(token)
                return token
        time.sleep(2)
        return self.get_token_by_login(login=login, search=search, attempt=attempt - 1)

    @allure_attach
    def delete_all_messages(self):
        response = self.client.delete(path='/api/v1/messages')
        return response

# if __name__ == "__main__":
#     MailhogApi().get_api_v2_messages(limit=2)
