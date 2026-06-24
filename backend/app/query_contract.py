from embeddings import generate_embeddings
from vector_store import retrieve_chunks

query="What level of care or diligence must the receiving party use to protect the secret data from leaking"

query_embedding=generate_embeddings(query)

results=retrieve_chunks(query_embedding)

for i, doc in enumerate(results["documents"][0], start=1):
    print(f"\nRESULT {i}\n")
    print(doc)