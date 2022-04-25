import fastapi
from fastapi import APIRouter

import schemas
import services

router = APIRouter()

@router.post("/chats")
async def create_chat(chat: schemas.ChatCreate, user: schemas.User = fastapi.Depends(services.get_current_user)):
    return await services.create_chat(chat, user)


@router.get("/chats")
async def get_chat(id1: int, id2: int, user: schemas.User = fastapi.Depends(services.get_current_user)):
    return await services.get_chat(id1, id2, user)


@router.delete("/chats")
async def delete_chat(id1: int, id2: int, user: schemas.User = fastapi.Depends(services.get_current_user)):
    return await services.delete_chat(id1, id2, user)