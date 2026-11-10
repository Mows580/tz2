from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from src.adapters.database.config import DatabaseConfig


def create_engine(config: DatabaseConfig) -> AsyncEngine:
    if not config.dsn:
        raise ValueError("APP_DB_DSN is not set")
    return create_async_engine(
        url=config.dsn,
        echo=config.echo,
    )

def create_sessionmaker(engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False,
        autoflush=False
    )

@asynccontextmanager
async def engine_lifespan(config: DatabaseConfig) -> AsyncIterator[AsyncEngine]:
    engine = create_engine(config)
    try:
        yield engine
    finally: 
        await engine.dispose()