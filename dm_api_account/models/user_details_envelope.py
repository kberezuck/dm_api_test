from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, StrictStr, Field, StrictBool
from datetime import datetime


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


class BbParseMode(Enum):
    COMMON = 'Common'
    INFO = 'Info'
    POST = 'Post'
    CHAT = 'Chat'


class InfoBbText(BaseModel):
    value: StrictStr
    parse_mode: List[BbParseMode]


class ColorSchema(Enum):
    MODERN = 'Modern'
    PALE = 'Pale'
    CLASSIC = 'Classic'
    CLASSIC_PALE = 'ClassicPale'
    NIGHT = 'Night'


class PagingSettings(BaseModel):
    posts_per_page: int = Field(alias="postsPerPage")
    comments_per_page: int = Field(alias="commentsPerPage")
    topics_per_page: int = Field(alias="topicsPerPage")
    messages_per_page: int = Field(alias="messagesPerPage")
    entities_per_page: int = Field(alias="entitiesPerPage")


class UserSettings(BaseModel):
    color_schema: List[ColorSchema]
    nanny_greetings_message: StrictStr = Field(alias="nannyGreetingsMessage")
    paging_settings: PagingSettings


class UserDetails(BaseModel):
    login: StrictStr
    roles: List[Roles]
    medium_picture_url: Optional[StrictStr] = Field(default=None, alias="mediumPictureUrl")
    small_picture_url: Optional[StrictStr] = Field(default=None, alias="smallPictureUrl")
    status: Optional[StrictStr] = Field(default=None)
    rating: Rating
    online: Optional[datetime] = Field(default=None)
    name: Optional[StrictStr] = Field(default=None)
    location: Optional[StrictStr] = Field(default=None)
    registration: Optional[datetime] = Field(default=None)
    icq: Optional[StrictStr] = Field(default=None)
    skype: Optional[StrictStr] = Field(default=None)
    original_picture_url: Optional[StrictStr] = Field(default=None, alias="originalPictureUrl")
    info: InfoBbText
    settings: UserSettings


class UserDetailsEnvelope(BaseModel):
    resource: UserDetails
    metadata: Optional[StrictStr] = Field(default=None)
