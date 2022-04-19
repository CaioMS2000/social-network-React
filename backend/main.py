# .\venv\Scripts\activate; uvicorn main:app --reload
# uvicorn main:app --reload
# cls; .\venv\Scripts\activate; uvicorn main:app --reload

import services
import fastapi
import fastapi.security
import typing

import database
import schemas
import models
from custom._OAuth2PasswordRequestForm import Custom_OAuth2PasswordRequestForm

app = fastapi.FastAPI()
database._metadata.create_all(database.engine)
app.state.database = database._database

@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()


@app.post("/user", response_model= dict)
async def create_user(user: schemas.UserCreate):
    db_user = await services.get_user(user.username)

    if db_user:
        raise fastapi.HTTPException(status_code=400, detail="Username not available")
    
    db_user = await services.get_user(user.email)

    if db_user:
        raise fastapi.HTTPException(status_code=400, detail="Email not available")
    
    db_user = await services.create_user(user)
    # return await services.create_token(user)
    return await services.create_token(db_user)


@app.post("/token", response_model= dict)
async def generate_token(form_data: Custom_OAuth2PasswordRequestForm = fastapi.Depends()):
# async def generate_token(form_data: fastapi.security.OAuth2PasswordRequestForm = fastapi.Depends()):
    user = await services.authenticate_user(form_data.username, form_data.password)
    # form_data.username -> não é necessariamente o username do usuario; é utilizado "username" apenas por ser padrão da biblioteca

    if not user:
        raise fastapi.HTTPException(status_code=401, detail="Invalid Credentials")
    
    return await services.create_token(user)


@app.get("/users/me", response_model= schemas.User)
async def get_user(user: schemas.User = fastapi.Depends(services.get_current_user)):
    return user


@app.get("/users", response_model= typing.List[schemas.User])
async def get_all_users():
    return await models.User.objects.all()


@app.post("/chats")
async def create_chat(chat: schemas.ChatCreate):
    return await services.create_chat(chat)


@app.get("/chats")
async def get_chat(id1: int, id2: int):
    return await services.get_chat(id1, id2)


@app.get("/comments")
async def get_comment(user_id: int, post_id: int):
    return await services.get_comment(user_id, post_id)


@app.post("/comments")
async def create_comment(comment: schemas.CommentCreate):
    return await services.create_comment(comment)


@app.get("/friendships")
async def get_friendship(receiver_id: int, sender_id: int):
    return await services.get_friendship(receiver_id, sender_id)


@app.post("/friendships")
async def create_friendship(friendship: schemas.FriendshipCreate):
    return await services.create_friendship(friendship)


@app.get("/likes")
async def get_like(post_id: int, user_id: int):
    return await services.get_like(post_id, user_id)


@app.post("/likes")
async def create_like(like: schemas.LikeCreate):
    return await services.create_like(like)


@app.get("/messages")
async def get_message(user_id: int, chat_id: int):
    return await services.get_message(user_id, chat_id)


@app.post("/messages")
async def create_message(message: schemas.MessageCreate):
    return await services.create_message(message)


@app.get("/posts")
async def get_post(id: int, user_id: int):
    return await services.get_post(id, user_id)


@app.post("/posts")
async def create_post(post: schemas.PostCreate):
    return await services.create_post(post)