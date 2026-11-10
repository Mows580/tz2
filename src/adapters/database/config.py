from dataclasses import dataclass, field
from os import environ


@dataclass(frozen=True, kw_only=True, slots=True)
class DatabaseConfig:
    dsn: str = field(default_factory=lambda: environ.get("APP_DB_DSN", ""))
    echo: bool = field(
        default_factory=lambda: environ.get("APP_DB_ECHO", "false").lower() == "true"
    )