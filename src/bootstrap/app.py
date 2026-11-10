from fastapi import FastAPI
from aiomisc.service.uvicorn import UvicornService
from contextlib import asynccontextmanager
from dishka.integrations.fastapi import setup_dishka
from dishka import make_async_container

from src.config import ApplicationConfig
from src.presenters.fastapi.api.router import router as api_router
from src.bootstrap.providers import AppProvider

class AppService(UvicornService):
    config: ApplicationConfig

    async def create_application(self) -> FastAPI:
        app = FastAPI(
            openapi_url="/docs/openapi.json",
            docs_url="/docs/swagger",
            redoc_url="/docs/redoc",
            lifespan=lifespan,
        )
        self.set_routers(app=app)
        self.set_dependencies(app=app)
        return app

    def set_routers(self, app: FastAPI) -> None:
        app.include_router(api_router)


    def set_dependencies(self, app: FastAPI) -> None:
        container = make_async_container(
            AppProvider(config=self.config),
        )
        setup_dishka(container=container, app=app)

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        yield
    finally:
        await app.state.dishka_container.close()
