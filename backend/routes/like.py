import fastapi
from fastapi import APIRouter

import schemas
import services

router = APIRouter(prefix= "/likes")

@router.get("")
async def get_like(post_id: int, user_id: int, user: schemas.User = fastapi.Depends(services.get_current_user)):
    return await services.get_like(post_id, user_id)


@router.post("")
async def create_like(like: schemas.LikeCreate, user: schemas.User = fastapi.Depends(services.get_current_user)):
    return await services.create_like(like, user)


@router.delete("/likes")
async def delete_like(post_id: int, user_id: int, user: schemas.User = fastapi.Depends(services.get_current_user)):
    return await services.delete_like(post_id, user_id, user)