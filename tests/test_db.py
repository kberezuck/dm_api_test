# import structlog
#
# from generic.helpers.orm_db import OrmDataBase
# from generic.helpers.orm_models import User
#
# structlog.configure(
#     processors=[
#         structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
#     ]
# )
#
#
# # подключаемся к  ORM
# def test_orm():
#     user = 'postgres'
#     password = 'admin'
#     host = 'localhost'
#     database = 'dm3.5'
#     orm = OrmDataBase(user=user, password=password, host=host, database=database)
#
#     dataset = orm.get_user_by_login('ksb010')
#     row: User
#     for row in dataset:
#         print(row.Login)
#         print(row.Email)
#         # print(row.Name)
#
#     orm.db.close_connection()
#
#     # dataset = connect.execute(text('select * from "public"."Users"')).fetchall()
#     # print(dataset)
#     # result = [dict(row) for row in dataset]
#     # print(result)
#
# # def test_db():
# #
# #     db = DmDataBase(user='postgres', password='admin', host='localhost', database='dm3.5')
# #     db.get_all_users()
