from hamcrest import assert_that


def test_post_v1_account(dm_api_facade, orm_db, prepare_user):
    login = prepare_user.login
    email = prepare_user.email
    password = prepare_user.password

    response = dm_api_facade.account.register_new_user(
        login=login,
        email=email,
        password=password,
        status_code=201
    )

    dataset = orm_db.get_user_by_login(login=login)
    for row in dataset:
        assert_that(row.Login == login, row.Activated is False)

    orm_db.activate_user(login=login)

    dataset = orm_db.get_user_by_login(login=login)

    for row in dataset:
        assert_that(row.Activated is True)

    dm_api_facade.login.login_user(
        login=login,
        password=password,
        status_code=200
    )
