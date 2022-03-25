# uvicorn main:app --reload
import fastapi
import fastapi.security
import sqlalchemy.orm
from datetime import datetime

import services
import models
import schemas

services.create_database()
app = fastapi.FastAPI()

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