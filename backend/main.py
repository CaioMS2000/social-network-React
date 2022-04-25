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
import routes

app = fastapi.FastAPI()
database._metadata.create_all(database.engine)
app.state.database = database._database

app.include_router(routes.user_router)
app.include_router(routes.post_router)
app.include_router(routes.message_router)
app.include_router(routes.chat_router)
app.include_router(routes.friendship_router)
app.include_router(routes.comment_router)
app.include_router(routes.like_router)

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


@app.post("/token", response_model= dict)
async def generate_token(form_data: Custom_OAuth2PasswordRequestForm = fastapi.Depends()):
# async def generate_token(form_data: fastapi.security.OAuth2PasswordRequestForm = fastapi.Depends()):
    user = await services.authenticate_user(form_data.username, form_data.password)
    # form_data.username -> não é necessariamente o username do usuario; é utilizado "username" apenas por ser padrão da biblioteca

    if not user:
        raise fastapi.HTTPException(status_code=401, detail="Invalid Credentials")
    
    return await services.create_token(user)