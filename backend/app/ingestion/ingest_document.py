from ingestion.pdf_extractor import extract_text_from_pdf
from ingestion.text_processor import clean_text
from ingestion.chunker import chunk_text

from embeddings import generate_embeddings
from storage.vector_store import store_chunks
from storage.chunk_store import save_chunks 

def ingest_document(pdf_path):
    try:
        text = extract_text_from_pdf(pdf_path)

        if text is None:
            return None

        cleaned_text = clean_text(text)

        if cleaned_text is None:
            return None

        chunks = chunk_text(cleaned_text)

        if chunks is None:
            return None
        
        save_chunks(chunks)

        embeddings = generate_embeddings(chunks)

        if embeddings is None:
            return None

        store_chunks(chunks, embeddings)

        return {
            "status": "success",
            "num_chunks": len(chunks)
        }

    except Exception as e:
        print(f"Ingestion Error: {e}")
        return None