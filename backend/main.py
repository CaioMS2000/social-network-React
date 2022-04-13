# .\venv\Scripts\activate; uvicorn main:app --reload
# uvicorn main:app --reload
# cls; .\venv\Scripts\activate; uvicorn main:app --reload

import services
import fastapi
import fastapi.security
from fastapi import Form

import database
import schemas
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


@app.post("/user")
async def create_user(user: schemas.UserCreate):
    db_user = await services.get_user(user.username)

    if db_user:
        raise fastapi.HTTPException(status_code=400, detail="Username not available")
    
    db_user = await services.get_user(user.email)

    if db_user:
        raise fastapi.HTTPException(status_code=400, detail="Email not available")
    
    return await services.create_user(user)


@app.post("/token")
async def generate_token(form_data: Custom_OAuth2PasswordRequestForm = fastapi.Depends()):
# async def generate_token(form_data: fastapi.security.OAuth2PasswordRequestForm = fastapi.Depends()):
    user = await services.authenticate_user(form_data.username, form_data.password)
    #extra = form_data.email
    # form_data.username -> não é necessariamente o username do usuario; é utilizado "username" apenas por ser padrão da biblioteca

    if not user:
        raise fastapi.HTTPException(status_code=401, detail="Invalid Credentials")
    
    return await services.create_token(user)


@app.get("/users/me")
async def get_user(user: schemas.User = fastapi.Depends(services.get_current_user)):
    return user


@app.post("/test")
async def test(username = Form(default=None, alias="username"), password = Form(default=None, alias="password"), email = Form(default=None, alias="emal"), full_name = Form(default=None, alias="full name")):
    d = {"username": username, "password": password, "email": email, "full_name": full_name}
    print(f"\n\n{d}\n\n", flush=True)
    pass