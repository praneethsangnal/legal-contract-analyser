from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "data"

CONTRACTS_DIR = DATA_DIR / "contracts"

CHROMA_DB_DIR = PROJECT_ROOT / "chroma_db"
