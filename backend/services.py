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


async def delete_user(user_id: int, user: schemas.User):
    if user_id != user.id:
        raise fastapi.HTTPException(status_code=401, detail="Invalid credentials")
        
    # try:
    #     await models.User.objects.delete(id= user_id)
    # except:
    #     raise fastapi.HTTPException(status_code=400, detail="Remove operation failed")
    obj = await models.User.objects.get_or_none(id= user_id)
    await models.User.remove()
    # await models.User.objects.delete(id= user_id)
#================ :USER =================================

#================ CHAT: =================================
async def get_chat(id1: int, id2: int, user: schemas.User):
    if user.id != id1 and user.id != id2:
        raise fastapi.HTTPException(status_code=401, detail="Invalid credentials")
    
    chat = await models.Chat.objects.get_or_none(first_id= id1, second_id= id2)

    if chat == None:
        chat = await models.Chat.objects.get_or_none(first_id= id2, second_id= id1)
    
    return chat


async def create_chat(chat: schemas.ChatCreate, user: schemas.User):
    if user.id != chat.first_id:
        raise fastapi.HTTPException(status_code=401, detail="Invalid credentials")

    chat = await models.Chat.objects.create(first_id= chat.first_id, second_id= chat.second_id)

    return chat


async def delete_chat(id1: int, id2: int, user: schemas.User):
    if user.id != id1 and user.id != id2:
        raise fastapi.HTTPException(status_code=401, detail="Invalid credentials")
    
    chat = await models.Chat.objects.get_or_none(first_id= id1, second_id= id2)
    if chat != None:
        await models.Chat.objects.delete(first_id= id1, second_id= id2)
        return
    
    chat = await models.Chat.objects.get_or_none(first_id= id2, second_id= id1)
    if chat != None:
        await models.Chat.objects.delete(first_id= id2, second_id= id1)
        return
    
    raise fastapi.HTTPException(status_code=400, detail="Remove operation failed")
#================ :CHAT =================================

#================ COMMENT: =================================
async def get_comment(user_id: int, post_id: int, user: schemas.User):
    comment = await models.Comment.objects.get_or_none(post_id= post_id, user_id= user_id)

    return comment


async def create_comment(comment: schemas.CommentCreate, user: schemas.User):
    if user.id != comment.user_id:
        raise fastapi.HTTPException(status_code=401, detail="Invalid credentials")

    comment = await models.Comment.objects.create(post_id= comment.post_id, user_id= comment.user_id, inner_text= comment.inner_text)

    return comment


async def delete_comment(user_id: int, post_id: int, user: schemas.User):
    if user_id != user.id:
        raise fastapi.HTTPException(status_code=401, detail="Invalid credentials")
    
    try:
        await models.Comment.objects.delete(user_id= user_id, post_id= post_id)
    except:
        raise fastapi.HTTPException(status_code=400, detail="Remove operation failed")
#================ :COMMENT =================================

#================ FRIENDSHIP: =================================
async def create_friendship(friendship: schemas.FriendshipCreate, user: schemas.User):
    if user.id != friendship.sender_id:
        raise fastapi.HTTPException(status_code=401, detail="Invalid credentials")

    friendship = await models.Friendship.objects.create(receiver_id= friendship.receiver_id, sender_id= friendship.sender_id)

    return friendship


async def get_friendship(receiver_id: int, sender_id: int, user: schemas.User):
    friendship = await models.Friendship.objects.get_or_none(receiver_id= receiver_id, sender_id= sender_id)

    if friendship == None:
        friendship = await models.Friendship.objects.get_or_none(receiver_id= sender_id, sender_id= receiver_id)

    return friendship


async def delete_friendship(id1: int, id2: int, user: schemas.User):
    if user.id != id1 and user.id != id2:
        raise fastapi.HTTPException(status_code=401, detail="Invalid credentials")
    
    friendship = await models.Friendship.objects.get_or_none(sender_id= id1, receiver_id= id2)

    if friendship != None:
        friendship = await models.Friendship.objects.delete(sender_id= id1, receiver_id= id2)
        return
    
    friendship = await models.Friendship.objects.get_or_none(sender_id= id2, receiver_id= id1)
    if friendship != None:
        friendship = await models.Friendship.objects.delete(sender_id= id2, receiver_id= id1)
    
    raise fastapi.HTTPException(status_code=400, detail="Remove operation failed")
#================ :FRIENDSHIP =================================

#================ LIKE: =================================
async def create_like(like: schemas.LikeCreate, user: schemas.User):
    if user.id != like.user_id:
        raise fastapi.HTTPException(status_code=401, detail="Invalid credentials")

    like = await models.Like.objects.create(post_id= like.post_id, user_id= like.user_id)

    return like


async def get_like(post_id: int, user_id: int, user: schemas.User):
    like = await models.Like.objects.get_or_none(post_id= post_id, user_id= user_id)

    return like


async def delete_like(post_id: int, user_id: int, user: schemas.User):
    if user.id != user_id:
        raise fastapi.HTTPException(status_code=401, detail="Invalid credentials")
    
    try:
        await models.Like.objects.delete(post_id= post_id, user_id= user_id)
    except:
        raise fastapi.HTTPException(status_code=400, detail="Remove operation failed")

#================ :LIKE =================================

#================ MESSAGE: =================================
async def get_message(user_id: int, chat_id: int, user: schemas.User):
    message = await models.Message.objects.get_or_none(chat_id= chat_id, user_id= user_id)

    return message


async def create_message(message: schemas.Message, user: schemas.User):
    if user.id != message.user_id:
        raise fastapi.HTTPException(status_code=401, detail="Invalid credentials")

    message = await models.Message.objects.create(user_id= message.user_id, chat_id= message.chat_id, inner_text= message.inner_text)

    return message


async def delete_message(user_id: int, chat_id: int, user: schemas.User):
    if user.id != user_id:
        raise fastapi.HTTPException(status_code=401, detail="Invalid credentials")
    
    try:
        await models.Message.objects.delete(chat_id= chat_id, user_id= user_id)
    except:
        raise fastapi.HTTPException(status_code=400, detail="Remove operation failed")
#================ :MESSAGE =================================


#================ POST: =================================
async def get_post(id: int, user_id: int, user: schemas.User):
    post = await models.Post.objects.get_or_none(id= id, user_id= user_id)

    return post


async def create_post(post: schemas.PostCreate, user: schemas.User):
    if user.id != post.user_id:
        raise fastapi.HTTPException(status_code=401, detail="Invalid credentials")

    post = await models.Post.objects.create(user_id= post.user_id, inner_text = post.inner_text)

    return post


async def delete_post(user_id: int, creation_data: str, user: schemas.User):
    try:
        await models.Post.objects.delete(user_id= user_id, created_at= creation_data)
    except:
        raise fastapi.HTTPException(status_code=400, detail="Remove operation failed")
#================ :POST =================================