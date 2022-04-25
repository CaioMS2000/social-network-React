import fastapi
from fastapi import APIRouter

import schemas
import services

router = APIRouter(prefix= "/comments")

@router.get("")
async def get_comment(user_id: int, post_id: int, user: schemas.User = fastapi.Depends(services.get_current_user)):
    return await services.get_comment(user_id, post_id)


@router.post("")
async def create_comment(comment: schemas.CommentCreate, user: schemas.User = fastapi.Depends(services.get_current_user)):
    return await services.create_comment(comment, user)


@router.delete("")
async def delete_comment(user_id: int, post_id: int, user: schemas.User = fastapi.Depends(services.get_current_user)):
    await services.delete_comment(user_id, post_id, user)