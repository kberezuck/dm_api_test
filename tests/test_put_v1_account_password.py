from hamcrest import assert_that


def test_put_v1_account_password(dm_api_facade, orm_db, prepare_user):
    login = prepare_user.login
    email = prepare_user.email
    password = prepare_user.password

    # Register new user
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

    # Login user
    dm_api_facade.login.login_user(
        login=login,
        password=password,
        status_code=200
    )

    # Get authorisation token and set headers
    token = dm_api_facade.login.get_auth_token(
        login=login,
        password=password,
        status_code=200
    )
    dm_api_facade.account.set_headers(headers=token)

    # Reset password
    dm_api_facade.account.reset_registered_user_password(
        login=login,
        email=email,
        status_code=200
    )

    # Change password
    new_password = 'qwerty1234'
    dm_api_facade.account.change_registered_user_password(
        login=login,
        old_password=password,
        new_password=new_password,
        status_code=200
    )
