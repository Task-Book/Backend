import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from database.dependency import get_database_session_factory
from database.provider import DatabaseProvider
from src.handlers import authorization, category, task


def configure_database(app: FastAPI) -> None:
    provider = DatabaseProvider(os.environ["SQLALCHEMY_DATABASE_URL"])
    app.dependency_overrides[
        get_database_session_factory
    ] = lambda: provider.session_factory


def configure_routes(app: FastAPI) -> None:
    app.include_router(authorization.router)
    app.include_router(task.router)
    app.include_router(category.router)


def create_app() -> FastAPI:
    app = FastAPI(
        title="Task Book", description="Convenient task management service"
    )
    app.mount("/static", StaticFiles(directory="static"), name="static")

    provider = DatabaseProvider(os.environ["SQLALCHEMY_DATABASE_URL"])
    app.dependency_overrides[
        get_database_session_factory
    ] = lambda: provider.session_factory
    configure_routes(app)

    return app