import pydantic

from .metaclasses import CONFIG

class UserBase(pydantic.BaseModel):
    email: str
    full_name: str
    username: str


class UserCreate(UserBase):
    hashed_password: str

    class Config(CONFIG):
        pass


class User(UserBase):
    id: int
    created_at: str
    profile_picture: str

    class Config(CONFIG):
        pass
