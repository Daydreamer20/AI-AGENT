from fastapi import FastAPI

from .config.settings import get_settings
from .config.logging_config import configure_logging
from .api.routes import router as api_router

settings = get_settings()
configure_logging("DEBUG" if settings.debug else "INFO")

app = FastAPI(title=settings.app_name, version=settings.version)

app.include_router(api_router)