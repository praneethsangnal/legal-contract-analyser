from config import CONTRACTS_DIR
from pdf_extractor import extract_text_from_pdf
from text_processor import clean_text
from chunker import chunk_text

pdf_path = CONTRACTS_DIR / "sample4.pdf"

text = extract_text_from_pdf(pdf_path)


cleaned_text=clean_text(text)

chunks=chunk_text(cleaned_text)

print(f"Number of chunks: {len(chunks)}")

for i, chunk in enumerate(chunks[:3]):
    print(f"\n--- CHUNK {i+1} ---\n")
    print(chunk)
