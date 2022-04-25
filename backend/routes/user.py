import fastapi
from fastapi import APIRouter
import typing

import schemas
import models
import services

router = APIRouter(prefix= "/users")

@router.post("", response_model= dict)
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


@router.get("/me", response_model= schemas.User)
async def get_user(user: schemas.User = fastapi.Depends(services.get_current_user)):
    return user


@router.get("", response_model= typing.List[schemas.User])
async def get_all_users(user: schemas.User = fastapi.Depends(services.get_current_user)):
    return await models.User.objects.all()


@router.delete("/{user_id}")
async def delete_user(user_id: int, user: schemas.User = fastapi.Depends(services.get_current_user)):
    return await services.delete_user(user_id, user)