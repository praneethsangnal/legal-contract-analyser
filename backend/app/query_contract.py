from retrieval.vector_retriever import search as vector_search
from retrieval.bm25_retriever import search as bm25_search
from retrieval.rrf import reciprocal_rank_fusion
from retrieval.reranker import rerank
from llm.question_answer import generate_answer
from llm.summary import generate_summary

query = "what is the termination period"

# print("\n===== VECTOR SEARCH =====\n")
vector_results = vector_search(query)


# print("\n===== BM25 SEARCH =====\n")
bm25_results = bm25_search(query)


# print("\n===== RRF SEARCH =====\n")
rrf_results = reciprocal_rank_fusion(
    vector_results,
    bm25_results
)

# print("\n===== FLASHRANK SEARCH =====\n")
reranked_results = rerank(
    query,
    rrf_results
)

# print("\n===== GROQ ANSWER =====\n")
answer=generate_answer(query,reranked_results)
print(answer)
print()


#print("summary")

summary=generate_summary()
print(summary)

