import allure

from db_client.db_client import DbClient


class DmDataBase:

    def __init__(self, user, password, host, database):
        self.db = DbClient(user, password, host, database)

    def get_all_users(self):
        with allure.step("Получение списка всех пользователей"):
            query = 'select * from "public"."Users"'
            dataset = self.db.send_query(query=query)
        return dataset

    def get_user_by_login(self, login):
        with allure.step("Получение данных о пользователе из базы"):
            query = f'''
            select * from "public"."Users"
            where "Login" = '{login}'
            '''
            dataset = self.db.send_query(query=query)
        return dataset

    def delete_user_by_login(self, login):
        with allure.step("Удаление пользователя с указанным логином"):
            query = f'''
            delete from "public"."Users" where "Login" = '{login}'
            '''
            dataset = self.db.send_bulk_query(query=query)
        return dataset

    def activate_user(self, login):
        with allure.step("Активация нового пользователя через базу данных"):
            query = f'''
                    update "public"."Users" set "Activated" = true where "Login" = '{login}'
                    '''
            dataset = self.db.send_bulk_query(query=query)
        return dataset
