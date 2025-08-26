from fastapi import APIRouter

from ..config.settings import get_settings

router = APIRouter()
settings = get_settings()


@router.get("/health")
def health() -> dict:
	return {"status": "ok", "version": settings.version}


@router.get("/config")
def get_config() -> dict:
	return settings.safe_dict()