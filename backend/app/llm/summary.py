from llm.groq_client import client
from storage.chunk_store import load_chunks


def generate_summary():

    chunks = load_chunks()

    if not chunks:
        return "No contract has been uploaded."

    try:

        context = "\n\n".join(chunks)

        system_prompt = (
            "You are an AI Legal Contract Assistant.\n"
            "Your task is to summarize the contract accurately.\n"
            "Use ONLY the information present in the contract.\n"
            "Do not make assumptions.\n\n"

            "Generate the summary using the following headings:\n"

            "1. Parties\n"
            "2. Purpose\n"
            "3. Key Obligations\n"
            "4. Confidentiality\n"
            "5. Termination\n"
            "6. Governing Law\n"
            "7. Important Clauses\n"
        )

        user_prompt = f"CONTRACT:\n\n{context}"

        response = client.chat.completions.create(

            model="llama-3.1-8b-instant",

            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],

            temperature=0,

            max_completion_tokens=1024

        )

        return response.choices[0].message.content

    except Exception as e:

        print(f"Summary Error: {e}")

        return None