from pydantic import BaseModel, StrictStr

class ChangePasswordModel(BaseModel):
    login: StrictStr
    token: StrictStr
    oldPassword: StrictStr
    newPassword: StrictStr
