from db_client.db_client import DbClient
class DmDataBase:

    def __init__(self, user, password, host, database):
        self.db = DbClient(user, password, host, database)

    def get_all_users(self):
        query = 'select * from "public"."Users"'
        dataset = self.db.send_query(query)
        return dataset
