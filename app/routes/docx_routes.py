from fastapi import APIRouter
from app.schemas.generate_request import GenerateRequest
from app.services.docx_service import DocxService
from app.services.image_service import download_drive_image
from app.utils.file_utils import delete_file

router = APIRouter()

@router.post("/generate")
def generate_docx(payload: GenerateRequest):
    doc = DocxService(template_path="templates/base_template.docx")
    
    if payload.text_replacements:
        doc.replace_text(payload.text_replacements)
    
    if payload.image_drive_id:
        image_path = download_drive_image(payload.image_drive_id)
        doc.replace_marker_with_image(marker="[IMAGEN]", image_path=image_path)
        delete_file(image_path)

    output_file = f"output/output_{payload.filename}.docx"
    doc.save(output_file)
    
    return {"status": "ok", "file": output_file}

@router.get("/hello")
def hello():
    return {"message": "Hello, World!"}
