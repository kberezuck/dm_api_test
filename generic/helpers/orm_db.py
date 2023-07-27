from typing import List

import allure
from sqlalchemy import select, update, delete

from generic.helpers.orm_models import User
from orm_client.orm_client import OrmClient


# def allure_attach(fn):
#     def wrapper(*args, **kwargs):
#         #         print(f"Смотри, что я получил:, {args}, {kwargs}")
#         query = kwargs.get('query')
#         print(f'query: {query}')
#         dataset = fn(*args, **kwargs)
#
#         #         # allure.attach(
#         #         #     query.compile(compile_kwargs={"literal_binds": True}),
#         #         #     name='request',
#         #         #     attachment_type=allure.attachment_type.JSON
#         #         # )
#         return dataset
#
#     return wrapper


class OrmDataBase:

    def __init__(self, user, password, host, database):
        self.db = OrmClient(user, password, host, database)

    # @allure_attach
    def get_all_users(self) -> List[User]:
        with allure.step("Получение списка всех пользователей"):
            query = select([User])
            dataset = self.db.send_query(query=query)
        return dataset

    # @allure_attach
    def get_user_by_login(self, login) -> List[User]:
        with allure.step("Получение данных о пользователе из базы"):
            query = select([User]).where(
                User.Login == login
            )
            dataset = self.db.send_query(query=query)
        return dataset

    # @allure_attach
    def delete_user_by_login(self, login):
        with allure.step("Удаление пользователя с указанным логином"):
            query = delete(User).where(
                User.Login == login
            )
            dataset = self.db.send_bulk_query(query=query)
        return dataset

    # @allure_attach
    def activate_user(self, login):
        with allure.step("Активация нового пользователя через базу данных"):
            query = update(User).where(
                User.Login == login
            ).values(
                {
                    User.Activated: True
                }
            )
            dataset = self.db.send_bulk_query(query=query)
        return dataset
