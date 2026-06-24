from rank_bm25 import BM25Okapi

from storage.chunk_store import load_chunks

def search(query, n_results=10):
    try:
        chunks = load_chunks()

        tokenized_chunks = [
            chunk.split()
            for chunk in chunks
        ]

        bm25 = BM25Okapi(tokenized_chunks)

        tokenized_query = query.split()

        scores = bm25.get_scores(tokenized_query)

        ranked_indices = sorted(
            range(len(scores)),
            key=lambda i: scores[i],
            reverse=True
        )[:n_results]

        results = [
            {
             "id": f"chunk_{i}",
             "document": chunks[i],
             "rank": rank
            }
            for rank,i in enumerate(
                ranked_indices,
                start=1
            )
        ]

        return results

    except Exception as e:
        print(f"BM25 Error: {e}")
        return None