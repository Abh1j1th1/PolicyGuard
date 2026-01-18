import io
from pypdf import PdfReader

def extract_text(file) -> list[str]:
    """
    Extracts text from a PDF file object. 
    Includes Cloud-Specific error handling.
    """
    try:
        # 1. CRITICAL: Reset cursor to the start of the file
        # Cloud servers sometimes read the file to check size, moving the cursor.
        file.seek(0)
        
        # 2. Read bytes into memory
        content = file.read()
        if not content:
            print("❌ Upload Error: File received was empty.")
            return []
            
        # 3. Create a BytesIO object for pypdf
        pdf_file = io.BytesIO(content)
        
        # 4. robust_reader helps with slightly corrupt PDFs
        reader = PdfReader(pdf_file, strict=False)
        
        pages = []
        # 5. Safe Iteration
        # We use len() range instead of direct iteration to catch IndexErrors
        num_pages = len(reader.pages)
        print(f"📄 Processing {num_pages} pages...")

        for i in range(num_pages):
            try:
                page = reader.pages[i]
                text = page.extract_text()
                
                if text:
                    # Clean up excessive whitespace
                    clean_text = " ".join(text.split())
                    pages.append(f"[Page {i+1}] {clean_text}")
            except Exception as e:
                # If one page fails, SKIP it. Do not crash the server.
                print(f"⚠️ Skipped Page {i+1} due to error: {e}")
                continue
                
        return pages

    except Exception as e:
        print(f"❌ Critical PDF Loader Error: {e}")
        return []