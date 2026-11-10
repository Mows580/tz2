from uuid import UUID

from src.presenters.fastapi.base_schemas import BaseSchema

class CompanyResponseSchema(BaseSchema):
    id: UUID
    name: str

class CompanyRequestSchema(BaseSchema):
    name: str