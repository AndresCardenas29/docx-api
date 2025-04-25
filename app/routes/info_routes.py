from fastapi import APIRouter
from app.core.config import settings

router = APIRouter()

@router.get("/")
def get_info():
    return {
      "version": settings.APP_VERSION,
      "name": settings.APP_NAME,
      "created_by": settings.CREATED_BY,
      "website_url": settings.WEBSITE_URL,
      "status": "ok",
    }