from dotenv import load_dotenv
import os

# cargar variables de entorno desde el archivo .env
load_dotenv()

class Settings:
	APP_NAME: str = os.getenv("APP_NAME", "DocxProcessor")
	APP_VERSION: str = os.getenv("APP_VERSION", "1.0.0")
	API_PREFIX: str = os.getenv("API_PREFIX", "/api/v1")
	HOST: str = os.getenv("HOST", "0.0.0.0")
	PORT: int = os.getenv("PORT", "5000")
	ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
	TEMPLATE_PATH: str = os.getenv("TEMPLATE_PATH", "templates/template.docx")

settings = Settings()