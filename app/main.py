from fastapi import FastAPI
from app.routes import docx_routes
from app.routes import info_routes
from app.core.config import settings

app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION)

app.include_router(
	docx_routes.router, 
	prefix=f"{settings.API_PREFIX}/docx", tags=["docx"]
)

app.include_router(
	info_routes.router, 
	prefix=f"{settings.API_PREFIX}/info", tags=["info"]
)
