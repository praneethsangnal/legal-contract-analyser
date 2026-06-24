from flashrank import Ranker, RerankRequest


ranker = Ranker()


def rerank(query, results, top_k=3):
    try:

        passages = [
            {
                "id": result["id"],
                "text": result["document"]
            }
            for result in results
        ]

        rerank_request = RerankRequest(
            query=query,
            passages=passages
        )

        reranked_results = ranker.rerank(
            rerank_request
        )

        return reranked_results[:top_k]

    except Exception as e:
        print(f"Reranking Error: {e}")
        return None