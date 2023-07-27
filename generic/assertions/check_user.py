import allure
from hamcrest import assert_that

from generic.helpers.orm_db import OrmDataBase


class AssertionsCheckUser:
    def __init__(self, orm_db: OrmDataBase):
        self.orm = orm_db

    def check_user_was_created(self, login):
        with allure.step("Проверка, что пользователь был создан"):
            dataset = self.orm.get_user_by_login(login=login)
            for row in dataset:
                assert_that(row.Login == login, row.Activated is False)

    def check_user_was_activated(self, login):
        with allure.step("Проверка, что пользователь был активирован"):
            dataset = self.orm.get_user_by_login(login=login)

            for row in dataset:
                assert_that(row.Activated is True)
