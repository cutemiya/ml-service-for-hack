from fastapi import APIRouter

from api.handler.analyze import base_router

main_router = APIRouter()
main_router.include_router(base_router, tags=['base'])
