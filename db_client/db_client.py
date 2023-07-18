import uuid

import records
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


class DbClient:
    def __init__(self, user, password, host, database, isolation_level="AUTOCOMMIT"):
        connection_string = f"postgresql://{user}:{password}@{host}/{database}"
        self.db = records.Database(connection_string, isolation_level=isolation_level)
        self.log = structlog.get_logger(self.__class__.__name__).bind(service="db")

# метод-обертка, логирующая запрос и ответ и принимающая на вход строку с sql запросом
    def send_query(self, query):
        print(query)
        log = self.log.bind(event_id=str(uuid.uuid4()))
        log.msg(
            event="request",
            query=query
        )
        dataset = self.db.query(query=query).as_dict()
        log.msg(
            event="response",
            dataset=dataset
        )
        return dataset

    # метод, необходимый для удаления записи из БД, который НИЧЕГО не возвращает. чисто апдейтит инфу в БД
    def send_bulk_query(self, query):
        print(query)
        log = self.log.bind(event_id=str(uuid.uuid4()))
        log.msg(
            event="request",
            query=query
        )
        self.db.bulk_query(query=query)

if __name__ == '__main__':

    db = DbClient(user='postgres', password='admin', host='localhost', database='dm3.5')
    query = 'select * from "public"."Users"'
    db.send_query(query)