from uuid import UUID
from dataclasses import dataclass

@dataclass(frozen=True, slots=True, kw_only=True)
class CompamyRequest:
    name: str

@dataclass(frozen=True, slots=True, kw_only=True)
class CompanyResponse:
    id: UUID
    name: str

@dataclass(frozen=True, kw_only=True, slots=True)
class CompanyList:
    company: CompanyResponse