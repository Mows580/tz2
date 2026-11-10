from uuid import UUID, uuid4

from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as PGUUID

from src.adapters.database.base import (
    BaseTable,
    IdentifiableMixin,
    TimestampedMixin,
)


class CompanyTable(BaseTable, IdentifiableMixin, TimestampedMixin):
    __tablename__ = "companies"

    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)