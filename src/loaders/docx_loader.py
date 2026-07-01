from docx import Document
import os

def load_docx(path):
    doc=Document(path)
    text="\n".join(
        p.text
        for p
        in doc.paragraphs
    )
    return [
        {
            "source":
                os.path.basename(path),
            "page": None,
            "text": text
        }
    ]