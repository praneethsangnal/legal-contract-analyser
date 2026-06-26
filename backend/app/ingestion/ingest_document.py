import time
import fitz

from ingestion.pdf_extractor import extract_text_from_pdf
from ingestion.ocr_extractor import extract_text_using_ocr
from ingestion.text_processor import clean_text
from ingestion.chunker import chunk_text

from embeddings import generate_embeddings
from storage.vector_store import store_chunks
from storage.chunk_store import save_chunks


def ingest_document(pdf_path):
    try:

        start_time = time.time()

        # Get page count
        document = fitz.open(pdf_path)
        page_count = len(document)
        document.close()

        extraction_method = "Text-based PDF"

        # First attempt normal PDF text extraction
        text = extract_text_from_pdf(pdf_path)

        if text is None:
            text = ""

        # Clean extracted text
        cleaned_text = clean_text(text)

        if cleaned_text is None:
            cleaned_text = ""

        # If very little readable text exists, switch to OCR
        if len(cleaned_text.strip()) < 100:
            print("No readable text found. Switching to OCR...")

            extraction_method = "Scanned PDF (OCR)"

            text = extract_text_using_ocr(pdf_path)

            if text is None:
                return None

            cleaned_text = clean_text(text)

            if cleaned_text is None:
                return None

        # Chunk the text
        chunks = chunk_text(cleaned_text)

        if chunks is None:
            return None

        # Save chunks for Summary / Risk Analysis
        save_chunks(chunks)

        # Generate embeddings
        embeddings = generate_embeddings(chunks)

        if embeddings is None:
            return None

        # Store embeddings in ChromaDB
        store_chunks(chunks, embeddings)

        processing_time = round(
            time.time() - start_time,
            2
        )

        return {
            "status": "success",
            "num_chunks": len(chunks),
            "page_count": page_count,
            "processing_time": processing_time,
            "extraction_method": extraction_method
        }

    except Exception as e:
        print(f"Ingestion Error: {e}")
        return None