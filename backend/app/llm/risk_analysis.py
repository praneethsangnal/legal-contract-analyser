from llm.groq_client import client
from storage.chunk_store import load_chunks


def generate_risk_analysis():

    chunks = load_chunks()

    if not chunks:
        return "No contract has been uploaded."

    try:

        context = "\n\n".join(chunks)

        system_prompt = (
            "You are an AI Legal Contract Risk Analyzer.\n\n"

            "Analyze ONLY the provided contract.\n"

            "Do not make assumptions that are unsupported by the contract.\n"

            "If a clause cannot be found, clearly state "
            "'Clause not found in the contract.'\n\n"

            "Generate a structured report using the following headings:\n\n"

            "1. Confidentiality\n"
            "- Risk Level (Low/Medium/High)\n"
            "- Explanation\n\n"

            "2. Liability\n"
            "- Risk Level\n"
            "- Explanation\n\n"

            "3. Termination\n"
            "- Risk Level\n"
            "- Explanation\n\n"

            "4. Intellectual Property\n"
            "- Risk Level\n"
            "- Explanation\n\n"

            "5. Governing Law\n"
            "- Risk Level\n"
            "- Explanation\n\n"

            "6. Missing or Ambiguous Clauses\n"
            "- Mention important clauses that appear to be missing or unclear based only on the provided contract.\n\n"

            "Keep the report concise and professional."
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

        print(f"Risk Analysis Error: {e}")

        return None