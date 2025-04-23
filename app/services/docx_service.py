from docx import Document
from docx.shared import Inches
from app.utils.file_utils import delete_file

class DocxService:
    def __init__(self, template_path: str):
        self.doc = Document(template_path)

    def replace_marker_with_image(self, marker: str, image_path: str):
        for table in self.doc.tables:
            for row in table.rows:
                for cell in row.cells:
                    if marker in cell.text:
                        cell.text = ""
                        run = cell.paragraphs[0].add_run()
                        run.add_picture(image_path, width=Inches(2.5))

    def replace_text(self, replacements: dict):
        for table in self.doc.tables:
            for row in table.rows:
                for cell in row.cells:
                    for key, value in replacements.items():
                        if key in cell.text:
                            cell.text = cell.text.replace(key, value)

    def save(self, output_path: str):
        self.doc.save(output_path)
