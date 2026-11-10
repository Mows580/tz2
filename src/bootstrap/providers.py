from collections.abc import AsyncIterable

from dishka import Provider, Scope, from_context, provide
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    AsyncEngine,
    async_sessionmaker
)

from src.adapters.database.config import DatabaseConfig
from src.adapters.database.repositories.company import CompanyRepository
from src.adapters.database.sessions import (
    create_sessionmaker,
    engine_lifespan,
)
from src.config import ApplicationConfig
from src.adapters.database.uow import UnitOfWork
from src.applications.interfaces.company_repository import ICompanyRepository
from src.applications.interfaces.uow import IUnitOfWork
from src.applications.usecases.company import CreateCompany

class AppProvider(Provider):
    def __init__(self, config: ApplicationConfig) -> None:
        super().__init__()
        self.config = config

    @provide(scope=Scope.APP)
    async def engine(self) -> AsyncIterable[AsyncEngine]:
        async with engine_lifespan(self.config.database) as engine:
            yield engine

    
    @provide(scope=Scope.APP)
    def session_facroty(
        self,
        engine: AsyncEngine,
    ) -> async_sessionmaker[AsyncSession]:
        return create_sessionmaker(engine)

    @provide(scope=Scope.REQUEST)
    async def session(
        self,
        factory: async_sessionmaker[AsyncSession],
    ) -> AsyncIterable[AsyncSession]:
        async with factory() as session:
            yield session

    company_repository = provide(
        CompanyRepository,
        provides=ICompanyRepository,
        scope=Scope.REQUEST
    )

    uow = provide(
        UnitOfWork,
        provides=IUnitOfWork,
        scope=Scope.REQUEST,
    )

    create_company = provide(
        CreateCompany,
        scope=Scope.REQUEST
    )