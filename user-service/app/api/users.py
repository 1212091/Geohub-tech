"""Controller to handle request for user service"""

from typing import List

from app.api import db_manager
from app.api.models import (UserActivityIn, UserActivityOut, UserIn, UserOut,
                            UserRoleIn, UserRoleOut)
from fastapi import APIRouter, HTTPException

users = APIRouter()


@users.post('/', response_model=UserOut, status_code=201)
async def create_user(payload: UserIn):
    """Create new user"""
    user_id = await db_manager.add_user(payload)
    response = {
        'id': user_id,
        **payload.dict()
    }
    return response


@users.post('/role', response_model=UserRoleOut, status_code=201)
async def create_user_role(payload: UserRoleIn):
    """Create new user role"""
    user_role_id = await db_manager.add_user_role(payload)
    response = {
        'id': user_role_id,
        **payload.dict()
    }
    return response


@users.post('/activity', status_code=201)
async def create_user_activity(payload: UserActivityIn):
    """Create new user activity"""
    user_activity_id = await db_manager.add_user_activity(payload)
    response = {
        'id': user_activity_id
    }
    return response


@users.get('/activity', response_model=List[UserActivityOut])
async def get_user_activities():
    """Get all user activities"""
    return await db_manager.get_all_user_activities()


@users.get('/{user_id}/', response_model=UserOut)
async def get_user(user_id: int):
    """Get user by user id"""
    user = await db_manager.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@users.get('/role/{role_id}/', response_model=UserRoleOut)
async def get_user_role(role_id: int):
    """Get user role by user role id"""
    user_role = await db_manager.get_user_role_by_id(role_id)
    if not user_role:
        raise HTTPException(status_code=404, detail="User role not found")
    return user_role
