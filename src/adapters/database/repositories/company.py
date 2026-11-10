from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession


from src.adapters.database.converters.company import convert_company_table_to_dto
from src.adapters.database.models.company import CompanyTable

from src.applications.interfaces.company_repository import ICompanyRepository
from src.applications.dto.company import (
    CompanyDTO,
    CreateCompanyDTO
)

class CompanyRepository(ICompanyRepository):

    def __init__(self, session: AsyncSession) -> None:
        self.__session = session

    async def create(self, *, create_dto: CreateCompanyDTO) -> CompanyDTO:
        stmt = (
            insert(CompanyTable)
            .values(
                name=create_dto.name
            )
            .returning(CompanyTable)
        )
        result = (await self.__session.scalars(stmt)).one()
        return convert_company_table_to_dto(result)