from fastapi import APIRouter
from app.api.routes.chat import agent_router

api_router = APIRouter()

api_router.include_router(agent_router)
