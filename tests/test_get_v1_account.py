import structlog

from services.dm_api_account import Facade

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)

def test_get_v1_account():
    api = Facade(host="http://localhost:5051")

    response = api.account.get_v1_account()


