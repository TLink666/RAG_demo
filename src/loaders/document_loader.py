import os
from src.loaders.txt_loader import load_txt
from src.loaders.pdf_loader import load_pdf
from src.loaders.docx_loader import load_docx
from src.loaders.md_loader import load_md

LOADERS={
    ".txt": load_txt,
    ".pdf": load_pdf,
    ".md": load_md,
    ".docx": load_docx
}

def load_documents(folder):
    docs=[]
    for file in os.listdir(folder):
        ext=os.path.splitext(file)[1]
        if (ext not in LOADERS):
            continue
        path=os.path.join(folder, file)
        docs.extend(LOADERS[ext](path))
    return docs