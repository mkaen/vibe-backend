from fastapi import APIRouter
from src.features.users.router import router_v1 as users_router_v1

api_router = APIRouter()

api_router.include_router(users_router_v1)

