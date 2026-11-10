from uuid import UUID, uuid4

from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as PGUUID

from src.adapters.database.base import (
    BaseTable,
    IdentifiableMixin,
    TimestampedMixin,
)


class ProductTable(BaseTable, IdentifiableMixin, TimestampedMixin):
    __tablename__ = "products"

    name: Mapped[str] = mapped_column(String(144), nullable=False, unique=True)
    count: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    company_id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("companies.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )
