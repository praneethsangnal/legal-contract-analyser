from ingestion.pdf_extractor import extract_text_from_pdf
from ingestion.ocr_extractor import extract_text_using_ocr
from ingestion.text_processor import clean_text
from ingestion.chunker import chunk_text

from embeddings import generate_embeddings
from storage.vector_store import store_chunks
from storage.chunk_store import save_chunks


def ingest_document(pdf_path):
    try:

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

        return {
            "status": "success",
            "num_chunks": len(chunks)
        }

    except Exception as e:
        print(f"Ingestion Error: {e}")
        return None