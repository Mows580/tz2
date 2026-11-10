from fastapi import APIRouter, Depends
from dishka.integrations.fastapi import DishkaRoute, FromDishka

from src.applications.dto.company import CreateCompanyDTO
from src.applications.usecases.company import CreateCompany

from src.presenters.fastapi.api.v1.schemas.company import (
    CompanyRequestSchema,
    CompanyResponseSchema
)

company_router = APIRouter(
    prefix="/company",
    tags=["Company"],
    route_class=DishkaRoute,
)

@company_router.post(
    "",
    response_model=CompanyResponseSchema,
    status_code=201,
)
async def create(
    *,
    data: CompanyRequestSchema,
    usecase: FromDishka[CreateCompany],
) -> CompanyResponseSchema:
    result = await usecase.execute(
        CreateCompanyDTO(name=data.name),
    )
    return CompanyResponseSchema.model_validate(result)