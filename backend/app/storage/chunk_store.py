import json

from config import PROCESSED_DIR


def save_chunks(chunks):
    try:
        PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

        chunks_file = PROCESSED_DIR / "chunks.json"

        with open(chunks_file, "w", encoding="utf-8") as file:
            json.dump(chunks, file, indent=4)

        print(f"{len(chunks)} chunks saved successfully")

    except Exception as e:
        print(f"Chunk Save Error: {e}")


def load_chunks():
    try:
        chunks_file = PROCESSED_DIR / "chunks.json"

        with open(chunks_file, "r", encoding="utf-8") as file:
            chunks = json.load(file)

        return chunks

    except Exception as e:
        print(f"Chunk Load Error: {e}")
        return None