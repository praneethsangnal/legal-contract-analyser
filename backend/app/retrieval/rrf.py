def reciprocal_rank_fusion(
    vector_results,
    bm25_results,
    k=60
):
    scores = {}

    documents = {}

    for result in vector_results:

        chunk_id = result["id"]

        rank = result["rank"]

        scores[chunk_id] = (
            scores.get(chunk_id, 0)
            + 1 / (k + rank)
        )

        documents[chunk_id] = result["document"]

    for result in bm25_results:

        chunk_id = result["id"]

        rank = result["rank"]

        scores[chunk_id] = (
            scores.get(chunk_id, 0)
            + 1 / (k + rank)
        )

        documents[chunk_id] = result["document"]

    fused_results = sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return [
        {
            "id": chunk_id,
            "document": documents[chunk_id],
            "rrf_score": score
        }
        for chunk_id, score in fused_results
    ]