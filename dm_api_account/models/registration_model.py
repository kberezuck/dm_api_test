from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field, StrictStr


# StrictStr - означает, что д.б строгое соответствие типу str
# если указать просто str, то какой бы тип данных не передавался - его преобразует в str


class Registration(BaseModel):
    class Config:
        extra = Extra.forbid

    login: Optional[StrictStr] = Field(None, description='Login')
    email: Optional[StrictStr] = Field(None, description='Email')
    password: Optional[StrictStr] = Field(None, description='Password')
