from dataclasses import dataclass, field

from src.adapters.database.config import DatabaseConfig


@dataclass(frozen=True, slots=True, kw_only=True)
class ApplicationConfig:
    database: DatabaseConfig = field(default_factory=DatabaseConfig)