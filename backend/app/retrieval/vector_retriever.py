from embeddings import generate_embeddings
from storage.vector_store import retrieve_chunks


def search(query, n_results=10):
    query_embedding = generate_embeddings(query)

    results = retrieve_chunks(
        query_embedding,
        n_results
    )

    formatted_results = []

    for rank, (chunk_id, document) in enumerate(
        zip(
            results["ids"][0],
            results["documents"][0]
        ),
        start=1
    ):
        formatted_results.append(
            {
                "id": chunk_id,
                "document": document,
                "rank": rank
            }
        )

    return formatted_results