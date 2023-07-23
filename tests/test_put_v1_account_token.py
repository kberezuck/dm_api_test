from hamcrest import assert_that, has_properties

from dm_api_account.models.user_envelope_model import UserRole


def test_put_v1_account_token(dm_api_facade, orm_db, prepare_user):
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

    # Get token from email
    token = dm_api_facade.mailhog.get_token_by_login(login=login, search='activate')
    response = dm_api_facade.account_api.put_v1_account_token(token=token, status_code=200)
    assert_that(response.resource, has_properties(
        {
            "login": login,
            "roles": [UserRole.guest, UserRole.player]
        }
    ))
