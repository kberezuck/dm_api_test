from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, StrictStr, Field, StrictBool, condate


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
    medium_picture_url: Optional[StrictStr] = Field(alias="mediumPictureUrl")
    small_picture_url: Optional[StrictStr] = Field(alias="smallPictureUrl")
    status: Optional[StrictStr]
    rating: Rating
    online: Optional[condate()]
    name: Optional[StrictStr]
    location: Optional[StrictStr]
    registration: Optional[condate()]


class UserEnvelopeModel(BaseModel):
    resource: User
    metadata: Optional[StrictStr]
