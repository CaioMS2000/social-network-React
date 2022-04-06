import pydantic

class _BASECLASS(pydantic.BaseModel):
    class Config(pydantic.BaseConfig):
        orm_mode = True


class _CREATIONCLASS():
    class Config(pydantic.BaseConfig):
        orm_mode = True