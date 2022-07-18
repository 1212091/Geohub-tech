from fastapi import APIRouter, HTTPException

from typing import List

from app.api.models import (
    UserOut,
    UserIn,
    UserRoleIn,
    UserRoleOut,
    UserActivityIn,
    UserActivityOut,
)
from app.api import db_manager

users = APIRouter()


@users.post('/', response_model=UserOut, status_code=201)
async def create_user(payload: UserIn):
    user_id = await db_manager.add_user(payload)
    response = {
        'id': user_id,
        **payload.dict()
    }
    return response


@users.post('/role', response_model=UserRoleOut, status_code=201)
async def create_user_role(payload: UserRoleIn):
    user_role_id = await db_manager.add_user_role(payload)
    response = {
        'id': user_role_id,
        **payload.dict()
    }
    return response


@users.post('/activity', status_code=201)
async def create_user_activity(payload: UserActivityIn):
    user_activity_id = await db_manager.add_user_activity(payload)
    response = {
        'id': user_activity_id
    }
    return response


@users.get('/activity', response_model=List[UserActivityOut])
async def get_user_activities():
    return await db_manager.get_all_user_activities()


@users.get('/{id}/', response_model=UserOut)
async def get_user(id: int):
    user = await db_manager.get_user_by_id(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@users.get('/role/{id}/', response_model=UserRoleOut)
async def get_user_role(id: int):
    user_role = await db_manager.get_user_role_by_id(id)
    if not user_role:
        raise HTTPException(status_code=404, detail="User role not found")
    return user_role