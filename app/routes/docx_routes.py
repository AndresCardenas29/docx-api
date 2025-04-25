from fastapi import APIRouter
from fastapi.responses import FileResponse
from app.schemas.generate_request import GenerateRequest
from app.services.docx_service import DocxService
from app.services.image_service import download_drive_image
from app.utils.file_utils import delete_file
from app.core.config import settings
template_path = settings.TEMPLATE_PATH

router = APIRouter()

@router.post("/generate")
def generate_docx(payload: GenerateRequest):
    doc = DocxService(template_path=template_path)
    
    if payload.text_replacements:
        doc.replace_text(payload.text_replacements)
    
    if payload.image_drive_id:
        image_path = download_drive_image(payload.image_drive_id)
        doc.replace_marker_with_image(marker="[IMAGEN]", image_path=image_path)
        delete_file(image_path)

    output_file = f"output/output_{payload.filename}.docx"
    doc.save(output_file)
    
    return {"status": "ok", "file": output_file}

@router.post("/get_formatting_options/")
def get_formatting_options(body: dict):
    
    name: str = body.get("name", "")
    email: str = body.get("email", "")
    phone: str = body.get("phone", "")
    mobile: str = body.get("mobile", "")
    address: str = body.get("address", "")
    website: str = body.get("website", "")
    sex: str = body.get("sex", "")
    birth: str = body.get("birth", "")
    nationality: str = body.get("nationality", "")
    work_position: str = body.get("work_position", "")
    work_experience: list = body.get("work_experience", [])
    education: list = body.get("education", [])
    native_language: str = body.get("native_language", "")
    languages: list = body.get("languages", [])
    communication_skill: str = body.get("communication_skill", "")
    job_skill: str = body.get("job_skill", "")
    digital_skill: list = body.get("digital_skill", [])
    organizational_skill: str = body.get("organizational_skill", "")
    driving_license: str = body.get("driving_license", "")
    other_skill: list = body.get("other_skill", [])
    additional_information: str = body.get("additional_information", "")
    imageID: str = body.get("imageID", "")
    
    doc = DocxService(template_path=template_path) 
    
    doc.formating_options()
    
    doc.replace_header_text({
        "[name]": name,
    })


    
    doc.replace_text({
        "[name]": name,
        "[email]": email,
        "[phone]": phone,
        "[mobile]": mobile,
        "[address]": address,
        "[website]": website,
        "[sex]": sex,
        "[birth]": birth,
        "[nationality]": nationality,
        "[work_position]": work_position,
        # Work date
        "[work.date]" : work_experience[0].get("init") + " - " + work_experience[0].get("end"),
        "[work.name]" : work_experience[0].get("business", ""),
        "[work.detail]" : work_experience[0].get("description", ""),
        # Education date
        "[edu.date]" : education[0].get("init") + " - " + education[0].get("end"),
        "[edu.name]" : education[0].get("university", ""),
        "[edu.detail]" : education[0].get("description", ""),
        "[tongue.mother]" : native_language,
        # Other language(s)
        "[Other language(s)]": languages[0].get("language", ""),
        "[tongue.listening]": languages[0].get("listening", ""),
        "[tongue.reading]": languages[0].get("reading", ""),
        "[tongue.spok.inter]": languages[0].get("spoken_interaction", ""),
        "[tongue.spok.prod]": languages[0].get("spoken_production", ""),
        "[tongue.writing]": languages[0].get("writing", ""),
        "[communication.skill]": communication_skill,
        "[organisational.skill]": organizational_skill,
        "[job.skills]": job_skill,
        "[self.infoprocess]": digital_skill.get("information_processing", ""),
        "[self.communic]": digital_skill.get("communication", ""),
        "[self.content]": digital_skill.get("content_creation", ""),
        "[self.safety]": digital_skill.get("safety", ""),
        "[self.probsolv]": digital_skill.get("problem_solving", ""),
        "[skills]": other_skill[0].get("description", ""),
    })
    
    image_path = download_drive_image(imageID)
    
    doc.replace_marker_with_image(marker="[IMAGE]", image_path=image_path)
    
    doc.save("output/temp.docx")
    
    doc.to_pdf("output/temp.docx")
    
    return FileResponse(
        path="output/temp.pdf",
        media_type="application/pdf",
        filename="temp.pdf",
    )
    
