from pydantic import BaseModel, StrictStr


class GeneralError(BaseModel):
    message: StrictStr
