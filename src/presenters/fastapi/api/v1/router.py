from fastapi import APIRouter

from src.presenters.fastapi.api.v1.endpoints.company import company_router

v1_router = APIRouter(prefix="/v1")

v1_router.include_router(company_router)
