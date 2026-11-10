from src.applications.interfaces.company_repository import ICompanyRepository
from src.applications.interfaces.uow import IUnitOfWork

from src.applications.dto.company import (
    CompanyDTO,
    CreateCompanyDTO
)

class CreateCompany:
    def __init__(
        self,
        repository: ICompanyRepository,
        uow: IUnitOfWork
    ) -> None:
        self.repository = repository
        self.uow = uow

    async def execute(self, dto: CreateCompanyDTO) -> CompanyDTO:
        async with self.uow:
            company = await self.repository.create(create_dto=dto)
        return company