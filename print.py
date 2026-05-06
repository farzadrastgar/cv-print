from docxtpl import DocxTemplate
import json

doc = DocxTemplate("./template/cv_template.docx")

with open("./data/cv.json") as f:
    context = json.load(f)

doc.render(context)
doc.save("./data/output_cv.docx")

