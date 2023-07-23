import json
import time

import structlog
from requests import Response

from restclient.restclient import Restclient

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


# def decorator(fn):
#     def wrapper(*args, **kwargs):
#         for i in range(5):
#             response = fn(*args, **kwargs)
#             emails = response.json()["items"]
#             if len(emails) < 5:
#                 print(f"attempt {i}")
#                 time.sleep(2)
#                 continue
#             else:
#                 return response
#
#     return wrapper()


class MailhogApi:
    def __init__(self, host="http://localhost:5025"):
        self.host = host
        self.client = Restclient(host=host)

    # @decorator
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

    def delete_all_messages(self):
        response = self.client.delete(path='/api/v1/messages')
        return response

# if __name__ == "__main__":
#     MailhogApi().get_api_v2_messages(limit=2)
