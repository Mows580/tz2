from dataclasses import dataclass
from uuid import UUID

@dataclass(frozen=True, slots=True, kw_only=True)
class CreateCompanyDTO:
    name: str

@dataclass(frozen=True, slots=True, kw_only=True)
class CompanyDTO:
    id: UUID
    name: str

