from pydantic import BaseModel
from typing import Optional, Dict

class GenerateRequest(BaseModel):
    filename: str
    text_replacements: Optional[Dict[str, str]] = None
    image_drive_id: Optional[str] = None
