from fastapi import APIRouter

from app.api.api_v1.endpoints import users, auth, airports, passengers, purchases

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(airports.router, prefix="/airposts", tags=["airposts"])
api_router.include_router(passengers.router, prefix='/passenger', tags=['passenger'])
api_router.include_router(purchases.router, prefix='/purchases', tags=['purchases'])

