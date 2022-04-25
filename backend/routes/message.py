import fastapi
from fastapi import APIRouter

import schemas
import services

router = APIRouter(prefix= "/messages")

@router.get("")
async def get_message(user_id: int, chat_id: int, user: schemas.User = fastapi.Depends(services.get_current_user)):
    return await services.get_message(user_id, chat_id)


@router.post("")
async def create_message(message: schemas.MessageCreate, user: schemas.User = fastapi.Depends(services.get_current_user)):
    return await services.create_message(message, user)


@router.delete("")
async def delete_message(user_id: int, chat_id: int, user: schemas.User = fastapi.Depends(services.get_current_user)):
    return await services.delete_message(user_id, chat_id, user)