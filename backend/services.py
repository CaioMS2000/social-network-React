import fastapi
import fastapi.security
import sqlalchemy.orm
import jwt
import os
from dotenv import load_dotenv
import passlib.hash

import database
import models
import schemas

load_dotenv()
JWT_SECRET = os.getenv("JWT_SECRET")
oauth2schema = fastapi.security.OAuth2PasswordBearer(tokenUrl="/token")
oauth2schema2 = fastapi.security.OAuth2PasswordBearer(tokenUrl="/test")

def wich_info(info: str) -> str:
    pos : int = info.find("@")

    return "email" if pos > -1 else "username"


async def authenticate_user(user_info: str, password: str):
    info: str = wich_info(user_info)
    db_user = None

    if info == "email":
        db_user = await models.User.objects.get_or_none(email= user_info)

    elif info == "username":
        db_user = await models.User.objects.get_or_none(username= user_info)
    
    if db_user == None:
        return False
    
    if not db_user.verify_password(password):
        return False
    
    return db_user


async def create_token(user: models.User):
    user_obj = schemas.User.from_orm(user)
    token = jwt.encode(user_obj.dict(), JWT_SECRET)

    return dict(access_token=token, token_type="bearer")


async def get_user(user_info: str):
    info: str = wich_info(user_info)

    if info == "email":
        return await models.User.objects.get_or_none(email= user_info)

    elif info == "username":
        return await models.User.objects.get_or_none(username= user_info)


async def create_user(user: schemas.UserCreate):
    user = await models.User.objects.create(email=user.email, hashed_password = passlib.hash.bcrypt.hash(user.hashed_password), full_name=user.full_name, username=user.username)

    return user


async def get_current_user(token: str = fastapi.Depends(oauth2schema)):
    print(f"\n\n{token}\n\n", flush=True)
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        user = payload["id"]
        
    except:
        raise fastapi.HTTPException(status_code=401, detail="Invalid credentials")
    
    print(f"\n\n{payload}\n{user}\n\n", flush=True)
    # return schemas.User.from_orm(user)
    usrfromorm = schemas.User.from_orm(payload)
    return usrfromorm