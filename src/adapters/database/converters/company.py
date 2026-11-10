from typing import Final

from adaptix.conversion import get_converter

from src.adapters.database.models.company import CompanyTable
from src.applications.dto.company import CompanyDTO

convert_company_table_to_dto: Final = get_converter(
    CompanyTable, CompanyDTO
)
