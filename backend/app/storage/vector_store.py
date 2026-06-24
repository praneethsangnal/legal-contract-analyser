import chromadb
from config import CHROMA_DB_DIR
client = chromadb.PersistentClient(path=str(CHROMA_DB_DIR))

collection = client.get_or_create_collection(
    name="legal_contracts"
)


def store_chunks(chunks, embeddings):
    try:
        ids = [f"chunk_{i}" for i in range(len(chunks))]

        collection.add(
            ids=ids,
            documents=chunks,
            embeddings=embeddings.tolist()
        )

        print(f"{len(chunks)} chunks stored successfully")

    except Exception as e:
        print(f"Storage Error: {e}")


def retrieve_chunks(query_embedding, n_results=5):
    try:
        results = collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=n_results
        )

        return results

    except Exception as e:
        print(f"Retrieval Error: {e}")
        return None