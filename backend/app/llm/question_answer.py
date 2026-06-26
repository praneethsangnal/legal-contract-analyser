from llm.groq_client import client

def generate_answer(query: str, reranked_results: list) -> str:
    if not reranked_results:
        return "I could not find any relevant text blocks to evaluate."

    try:
        context = "\n\n".join(
            f"--- [Contract Text Block {i+1}] ---\n{result['text']}" 
            for i, result in enumerate(reranked_results)
        )

        system_prompt = (
            "You are a precise, literal AI Legal Contract Assistant.\n"
            "Your sole objective is to answer the user's question using ONLY the provided contract text blocks.\n\n"
            "STRICT RULES:\n"
            "1. Rely only on clear facts directly mentioned in the text. Do not make assumptions or extensions.\n"
            "2. If the answer cannot be explicitly found within the context blocks, you must reply exactly with: "
            "'I could not find this information in the contract.' Do not append any alternative explanations."
        )

        user_prompt = f"CONTRACT CONTEXT:\n{context}\n\nUSER QUESTION:\n{query}"

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0,
            max_completion_tokens=1024
        )

        return response.choices[0].message.content

    except Exception as e:
        print(f"Groq Orchestration Error: {e}")
        return None