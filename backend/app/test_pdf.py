from config import CONTRACTS_DIR
from pdf_extractor import extract_text_from_pdf

pdf_path = CONTRACTS_DIR / "sample1.pdf"

text = extract_text_from_pdf(pdf_path)

if text:
    print(text[:3000])
else:
    print("Extraction failed")