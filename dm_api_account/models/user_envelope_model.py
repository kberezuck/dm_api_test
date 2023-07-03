from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, StrictStr, Field, StrictBool, AwareDatetime


# в pydantic все поля - обязательные и если нам в ответе от сервера какое-то поле не придет - упадет ошибка.
# чтобы этого избежать используем тип "Optional". Все классы- это переменные с "вложенной структурой" (см. свагер sheme)
# №все значения указаны там же ( узнать, является ли поле необязательным - опытным путем по ответу от сервера. где упадет из-за отсутствия значения , там и ставим)


class Roles(Enum):
    GUEST = "Guest"
    PLAYER = "Player"
    ADMINISTRATOR = "Administrator"
    NANNY_MODERATOR = "NannyModerator"
    REGULAR_MODERATOR = "RegularModerator"
    SENIOR_MODERATOR = 'SeniorModerator'


class Rating(BaseModel):
    enabled: StrictBool
    quality: int
    quality: int


class User(BaseModel):
    login: StrictStr
    roles: List[Roles]
    medium_picture_url: Optional[StrictStr] = Field(default=None, alias="mediumPictureUrl")
    small_picture_url: Optional[StrictStr] = Field(default=None, alias="smallPictureUrl")
    status: Optional[StrictStr] = Field(default=None)
    rating: Rating
    online: Optional[AwareDatetime] = Field(default=None)
    name: Optional[StrictStr] = Field(default=None)
    location: Optional[StrictStr] = Field(default=None)
    registration: Optional[AwareDatetime] = Field(default=None)


class UserEnvelopeModel(BaseModel):
    resource: Optional[User] = Field(default=None)
    metadata: Optional[StrictStr] = Field(default=None)
