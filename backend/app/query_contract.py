from retrieval.vector_retriever import search as vector_search
from retrieval.bm25_retriever import search as bm25_search
from retrieval.rrf import reciprocal_rank_fusion
from retrieval.reranker import rerank

query = "What are the confidentiality obligations of the receiving party?"

print("\n===== VECTOR SEARCH =====\n")

vector_results = vector_search(query)

for result in vector_results:
    print(result["id"], result["rank"])



print("\n===== BM25 SEARCH =====\n")

bm25_results = bm25_search(query)

for result in bm25_results:
    print(result["id"], result["rank"])


print("\n===== RRF SEARCH =====\n")

rrf_results = reciprocal_rank_fusion(
    vector_results,
    bm25_results
)

for result in rrf_results[:10]:
    print(result["id"])


print("\n===== FLASHRANK SEARCH =====\n")

reranked_results = rerank(
    query,
    rrf_results
)

for result in reranked_results:
    print(result)