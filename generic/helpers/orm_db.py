from typing import List

from sqlalchemy import select, update, delete

from generic.helpers.orm_models import User
from orm_client.orm_client import OrmClient


class OrmDataBase:

    def __init__(self, user, password, host, database):
        self.db = OrmClient(user, password, host, database)

    def get_all_users(self) -> List[User]:
        query = select([User])
        dataset = self.db.send_query(query)
        return dataset

    def get_user_by_login(self, login) -> List[User]:
        query = select([User]).where(
            User.Login == login
        )
        dataset = self.db.send_query(query)
        return dataset

    def delete_user_by_login(self, login):
        query = delete(User).where(
            User.Login == login
        )
        dataset = self.db.send_bulk_query(query=query)
        return dataset

    def activate_user(self, login):
        query = update(User).where(
            User.Login == login
        ).values(
            {
                User.Activated: True
            }
        )
        dataset = self.db.send_bulk_query(query=query)
        return dataset
