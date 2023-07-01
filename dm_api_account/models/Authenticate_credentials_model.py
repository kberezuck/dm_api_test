from pydantic import BaseModel, StrictStr, StrictBool


class AuthenticateCredentialsModel(BaseModel):
    login: StrictStr
    password: StrictStr
    rememberMe: StrictBool
