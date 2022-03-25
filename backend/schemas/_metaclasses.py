import pydantic

class _BASECLASS(pydantic.BaseModel):
    pass


class _CREATIONCLASS():
    class Config:
        orm_mode = True