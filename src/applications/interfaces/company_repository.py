from uuid import UUID
from typing import Protocol

from src.applications.dto.company import (
    CompanyDTO,
    CreateCompanyDTO
)

class ICompanyRepository(Protocol):

    async def create(self, *, create_dto: CreateCompanyDTO) -> CompanyDTO: ...

    async def get_by_id(self, *, company_id: UUID) -> CompanyDTO: ...

    async def list(self) -> list[CompanyDTO]: ...