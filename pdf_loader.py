import io
from PyPDF2 import PdfReader

def extract_text(file) -> list[str]:
    """
    Extracts text from a PDF file object. Returns a list of strings (one per page).
    """
    try:
        file.seek(0)
        content = file.read()
        pdf_file = io.BytesIO(content)
        reader = PdfReader(pdf_file)
        
        pages = []
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text:
                clean_text = " ".join(text.split())
                pages.append(f"[Page {i+1}] {clean_text}")
                
        return pages
    except Exception as e:
        print(f"❌ PDF Error: {e}")
        return []