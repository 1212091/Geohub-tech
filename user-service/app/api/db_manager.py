"""Handle CRUD operation for user service"""
import datetime

from app.api.db import database, user_activity, user_role, users
from app.api.models import UserActivity, UserActivityIn, UserIn, UserRoleIn


async def add_user(payload: UserIn):
    """Add user to database"""
    query = users.insert().values(**payload.dict())
    return await database.execute(query=query)


async def add_user_role(payload: UserRoleIn):
    """Add user role to database"""
    query = user_role.insert().values(**payload.dict())
    return await database.execute(query=query)


async def add_user_activity(user_activity_input: UserActivityIn):
    """Add user activity to database"""
    user_activity_model = UserActivity(
        user_id=user_activity_input.user_id,
        action=user_activity_input.action,
        timestamp=datetime.datetime.now()
    )
    query = user_activity.insert().values(**user_activity_model.dict())
    return await database.execute(query=query)


async def get_all_user_activities():
    """Get all user activities"""
    query = user_activity.select()
    return await database.fetch_all(query=query)


async def get_user_by_id(user_id: int):
    """Get user by id"""
    query = users.select(users.c.id == user_id)
    return await database.fetch_one(query=query)


async def get_user_role_by_id(user_role_id: int):
    """Get user role by id"""
    query = user_role.select(user_role.c.id == user_role_id)
    return await database.fetch_one(query=query)
