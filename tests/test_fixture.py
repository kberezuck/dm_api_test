#
# from hamcrest import assert_that, has_entries
#
#
# def test_post_v1_account(dm_api_facade, dm_db, prepare_user):
#     login = prepare_user.login
#     email = prepare_user.email
#     password = prepare_user.password
#
#     # Register new user
#     response = dm_api_facade.account.register_new_user(
#         login=login,
#         email=email,
#         password=password
#     )
#
#     # получение юзера по логину, для проверки наличия записи в БД
#
#     dataset = dm_db.get_user_by_login(login=login)
#     for row in dataset:
#         assert_that(row, has_entries(
#             {
#                 'Login': login,
#                 'Activated': False
#             }
#         ))
#
#     # Register activate_user
#     dm_db.activate_user(login=login)
#     # dm_api_facade.account.activate_registered_user(login=login)
#     # time.sleep(2)
#     #
#
#     dataset = dm_db.get_user_by_login(
#         login=login)  # перезапрашиваем данные из БЗ, чтобы прочекать внесенные в ней изменения
#
#     # проверка, что юзер активирован
#     for row in dataset:
#         assert_that(row, has_entries(
#             {
#                 'Activated': True
#             }
#         ))
#
#     # Login user
#     dm_api_facade.login.login_user(
#         login=login,
#         password=password
#     )
#
#
# # @pytest.mark.parametrize('login, email, password', [
# #     ('ksb123', 'ksb123@mail.ru', 'qwerty1234'),
# #     ('login', 'ksb@mail.ru', '13245'),
# #     ('132564848', '13215464@mail.ru', '!!!!!!!!!'),
# #     ('||||||||||', '//////////@mail.ru', '!!!!!!!!!'),
# # ])
#
