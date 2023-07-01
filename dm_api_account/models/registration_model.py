from pydantic import BaseModel, StrictStr  # StrictStr - означает, что д.б строгое соответствие типу str


# если указать просто str, то какой бы тип данных не передавался - его преобразует в str


class RegistrationModel(BaseModel):
    login: StrictStr
    email: StrictStr
    password: StrictStr
