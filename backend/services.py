import email
import sqlalchemy.orm
import jwt
import os
from dotenv import load_dotenv
import passlib.hash

import _database
import models
import schemas

load_dotenv()
JWT_SECRET = os.getenv("JWT_SECRET")

def wich_info(info: str) -> str:
    pos : int = info.find("@")

    return "email" if pos > -1 else "username"


def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)


def get_database():
    db = _database.SessionLocal()

    try:
        return db
    finally:
        db.close()

async def authenticate_user(db: sqlalchemy.orm.Session):
    pass


async def create_token():
    token = jwt.encode({}, JWT_SECRET)

    return dict(access_token=token, token_type="bearer")


async def get_user(user_info: str, db: sqlalchemy.orm.Session):
    info: str = wich_info(user_info)

    if info == "email":
        return db.query(models.User).filter(models.User.email == user_info).first()

    elif info == "username":
        return db.query(models.User).filter(models.User.username == user_info).first()


async def create_user(user: schemas.UserCreate, db: sqlalchemy.orm.Session):
    user = models.User(email=user.email, hashed_password = passlib.hash.bcrypt.hash(user.hashed_password))

    db.add(user)
    db.commit()
    db.refresh(user)

    return user