from pydantic import BaseModel, StrictStr, UUID4


class ChangePasswordModel(BaseModel):
    login: StrictStr
    token: UUID4
    oldPassword: StrictStr
    newPassword: StrictStr
