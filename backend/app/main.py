from config import CONTRACTS_DIR
from ingestion.ingest_document import ingest_document

pdf_path = CONTRACTS_DIR / "sample4.pdf"

result = ingest_document(pdf_path)

print(result)