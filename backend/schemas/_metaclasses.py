import pydantic

class _BASECLASS(pydantic.BaseModel):
    class Config(pydantic.BaseConfig):
        orm_mode = True
        allow_population_by_field_name = True


class _CREATIONCLASS(pydantic.BaseModel):
    class Config(pydantic.BaseConfig):
        orm_mode = True
        allow_population_by_field_name = True