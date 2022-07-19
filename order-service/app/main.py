from fastapi import FastAPI

from app.api.db import database, engine, metadata
from app.api.orders import orders

metadata.create_all(engine)

app = FastAPI(openapi_url="/api/v1/orders/openapi.json",
              docs_url="/api/v1/orders/docs")


@app.on_event("startup")
async def startup():
    """Start up service event"""
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    """Shut down service event"""
    await database.disconnect()

app.include_router(orders, prefix='/api/v1/orders', tags=['orders'])
