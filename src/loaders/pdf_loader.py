from pypdf import PdfReader

def load_pdf(path):
    reader = PdfReader(path)
    pages = []
    for page_num, page in enumerate(reader.pages):
        text = page.extract_text()
        pages.append({
            "page": page_num + 1,
            "text": text
        })
    return pages