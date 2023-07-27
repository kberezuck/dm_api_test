from __future__ import annotations

import allure
import requests
from pydantic import BaseModel


def validate_request_json(json: str | BaseModel):
    with allure.step("Проверка на соответсвие Json - BaseModel"):
        if isinstance(json, dict):
            return json
        return json.model_dump(by_alias=True, exclude_none=True)


def validate_status_code(response: requests.Response, status_code: int):
    """
    :param response:
    :type status_code: object
    """
    with allure.step("Проверка ответа сервера и статус кода"):
        assert response.status_code == status_code, \
            f"Ожидался статус код {status_code}, а фактически {response.status_code}"
