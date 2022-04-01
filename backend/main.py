# uvicorn main:app --reload
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

@app.post("/api/token")
async def generate_token(form_data: fastapi.security.OAuth2PasswordRequestForm = fastapi.Depends(), db: sqlalchemy.orm.Session = fastapi.Depends(services.get_database)):
    user = dict(username=form_data.username, password=form_data.password)
    valid = True

    if not valid:
        raise fastapi.HTTPException(status_code=401, detail="Invalid Credentials")
    
    return await services.create_token()


@app.post("/user")
async def create_user(user: schemas.UserCreate, db: sqlalchemy.orm.Session = fastapi.Depends(services.get_database)):
    user = await services.get_user(user.username, db)

    if user:
        raise fastapi.HTTPException(status_code=400, detail="Username not available")
    
    user = await services.get_user(user.email, db)

    if user:
        raise fastapi.HTTPException(status_code=400, detail="Email not available")
    

    return await services.create_user(user, db)