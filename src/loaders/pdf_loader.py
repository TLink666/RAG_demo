from pypdf import PdfReader
import os

def load_pdf(path):
    reader=PdfReader(path)
    pages=[]
    for i,page in enumerate(reader.pages,1):
        pages.append({
            "source":
                os.path.basename(path),
            "page": i,
            "text":
                page
                .extract_text()
                or
                ""
        })
    return pages