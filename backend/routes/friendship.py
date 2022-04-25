import fastapi
from fastapi import APIRouter

import schemas
import services

router = APIRouter(prefix= "/friendship")

@router.get("")
async def get_friendship(receiver_id: int, sender_id: int, user: schemas.User = fastapi.Depends(services.get_current_user)):
    return await services.get_friendship(receiver_id, sender_id)


@router.post("")
async def create_friendship(friendship: schemas.FriendshipCreate, user: schemas.User = fastapi.Depends(services.get_current_user)):
    return await services.create_friendship(friendship, user)


@router.delete("")
async def delete_friendship(id1: int, id2: int, user: schemas.User = fastapi.Depends(services.get_current_user)):
    return await services.delete_friendship(id1, id2, user)