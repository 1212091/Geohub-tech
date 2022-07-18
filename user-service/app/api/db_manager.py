import datetime

from app.api.models import UserIn, UserRoleIn, UserActivityIn, UserActivity
from app.api.db import users, user_role, user_activity, database

async def add_user(payload: UserIn):
    query = users.insert().values(**payload.dict())
    return await database.execute(query=query)

async def add_user_role(payload: UserRoleIn):
    query = user_role.insert().values(**payload.dict())
    return await database.execute(query=query)

async def add_user_activity(user_activity_input: UserActivityIn):
    user_activity_model = UserActivity(
        user_id=user_activity_input.user_id,
        action=user_activity_input.action,
        timestamp=datetime.datetime.now()
    )
    query = user_activity.insert().values(**user_activity_model.dict())
    return await database.execute(query=query)

async def get_all_user_activities():
    query = user_activity.select()
    return await database.fetch_all(query=query)

async def get_user_by_id(id):
    query = users.select(users.c.id==id)
    return await database.fetch_one(query=query)

async def get_user_role_by_id(id):
    query = user_role.select(user_role.c.id==id)
    return await database.fetch_one(query=query)