# .\venv\Scripts\activate; uvicorn main:app --reload
# uvicorn main:app --reload
import os
# os.system('cls')
# cls; .\venv\Scripts\activate; uvicorn main:app --reload

import fastapi
import fastapi.security
import sqlalchemy.orm
from datetime import datetime

import services
import database
import schemas

services.create_database()
app = fastapi.FastAPI()
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
async def create_user(user: schemas.UserCreate, db: sqlalchemy.orm.Session = fastapi.Depends(services.get_database)):
    db_user = await services.get_user(user.username, db)

    if db_user:
        raise fastapi.HTTPException(status_code=400, detail="Username not available")
    
    db_user = await services.get_user(user.email, db)

    if db_user:
        raise fastapi.HTTPException(status_code=400, detail="Email not available")
    
    return await services.create_user(user, db)


@app.post("/token")
async def generate_token(form_data: fastapi.security.OAuth2PasswordRequestForm = fastapi.Depends(), db: sqlalchemy.orm.Session = fastapi.Depends(services.get_database)):
    user = await services.authenticate_user(form_data.username, form_data.password, db)
    # form_data.username -> não é necessariamente o username do usuario; é utilizado "username" apenas por ser padrão da biblioteca

    if not user:
        raise fastapi.HTTPException(status_code=401, detail="Invalid Credentials")
    
    return await services.create_token(user)
    """
    user = dict(username=form_data.username, password=form_data.password)
    valid = True

    if not valid:
        raise fastapi.HTTPException(status_code=401, detail="Invalid Credentials")
    
    return await services.create_token()
    """
