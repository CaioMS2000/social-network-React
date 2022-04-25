import fastapi
from fastapi import APIRouter

import schemas
import services

router = APIRouter(prefix= "/posts")

@router.get("")
async def get_post(id: int, user_id: int, user: schemas.User = fastapi.Depends(services.get_current_user)):
    return await services.get_post(id, user_id)


@router.post("")
async def create_post(post: schemas.PostCreate, user: schemas.User = fastapi.Depends(services.get_current_user)):
    return await services.create_post(post)


@router.delete("")
async def delete_post(user_id: int, creation_data: str, user: schemas.User = fastapi.Depends(services.get_current_user)):
    return await services.delete_post(user_id, creation_data, user)