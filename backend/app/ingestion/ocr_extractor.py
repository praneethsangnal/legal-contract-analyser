import fitz
import pytesseract
from PIL import Image
import io
import gc

def extract_text_using_ocr(pdf_path):
    try:
        document = fitz.open(pdf_path)
        extracted_pages = []

        for page_number in range(len(document)):
            page = document.load_page(page_number)
            pix = page.get_pixmap(dpi=150)
            
            img_data = pix.tobytes("png")
            image = Image.open(io.BytesIO(img_data))
            
            page_text = pytesseract.image_to_string(image)
            extracted_pages.append(page_text)
            
            del pix
            del img_data
            del image
            del page
            gc.collect()

        document.close()
        return "\n\n".join(extracted_pages)

    except Exception as e:
        print(f"OCR Extraction Error: {e}")
        return None