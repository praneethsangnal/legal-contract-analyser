from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)


def generate_embeddings(chunks):
    try:
        if not chunks:
            return None

        embeddings = model.encode(chunks)

        return embeddings

    except Exception as e:
        print(f"Embedding Error: {e}")
        return None