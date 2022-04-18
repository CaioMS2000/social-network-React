import fastapi
import fastapi.security
import jwt
import os
from dotenv import load_dotenv
import passlib.hash

import models
import schemas

load_dotenv()
JWT_SECRET = os.getenv("JWT_SECRET")
oauth2schema = fastapi.security.OAuth2PasswordBearer(tokenUrl="/token")#a presença disso que habilita a autentição

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


#================ USER: =================================
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
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        user = await models.User.objects.get_or_none(id= payload["id"])
        
    except:
        raise fastapi.HTTPException(status_code=401, detail="Invalid credentials")
    

    return schemas.User.from_orm(user)
#================ :USER =================================

#================ CHAT: =================================
async def get_chat(id1: int, id2: int):
    chat = await models.Chat.objects.get_or_none(first_id= id1, second_id= id2)

    if chat == None:
        chat = await models.Chat.objects.get_or_none(first_id= id2, second_id= id1)
    
    return chat
#================ :CHAT =================================