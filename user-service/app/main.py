from fastapi import FastAPI

from app.api.db import database, engine, metadata
from app.api.users import users

metadata.create_all(engine)

app = FastAPI(openapi_url="/api/v1/users/openapi.json",
              docs_url="/api/v1/users/docs")


@app.on_event("startup")
async def startup():
    """Start up service event"""
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    """Shut down service event"""
    await database.disconnect()

app.include_router(users, prefix='/api/v1/users', tags=['users'])
