from enum import Enum
from typing import Optional, List

from pydantic import BaseModel, StrictStr, Field


# class InvalidProperties(BaseModel):
# additional_Prop1: StrictStr = Field(alias="additionalProp1")  # может лист??
# additional_Prop2: StrictStr = Field(alias="additionalProp2")
# additional_Prop3: StrictStr = Field(alias="additionalProp3")

class InvalidProperties(Enum):
    ADDITIONAL_PROP1 = "additionalProp1"
    ADDITIONAL_PROP2 = "additionalProp2"
    ADDITIONAL_PROP3 = "additionalProp3"


class BadRequestModel(BaseModel):
    message: Optional[StrictStr] = Field(default=None)
    invalidProperties: List[InvalidProperties]
