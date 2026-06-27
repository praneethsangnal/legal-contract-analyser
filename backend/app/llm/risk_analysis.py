from app.llm.groq_client import client
from app.storage.chunk_store import load_chunks


def generate_risk_analysis():

    chunks = load_chunks()

    if not chunks:
        return "No contract has been uploaded."

    try:

        context = "\n\n".join(chunks)

        system_prompt = (
    "You are an expert AI Legal Contract Risk Analyzer.\n\n"

    "Analyze ONLY the provided contract.\n"
    "Do not make assumptions that are unsupported by the contract.\n"
    "If a clause cannot be identified, explicitly state "
    "'Clause not found in the contract.'\n\n"

    "Generate a professional risk analysis report using EXACTLY the following format.\n\n"

    "For EVERY section, provide:\n"
    "• Risk Level (Low / Medium / High)\n"
    "• Explanation\n"
    "• Recommendation\n\n"

    "Recommendation Rules:\n"
    "1. If the risk is Low, state that no changes are recommended.\n"
    "2. If the risk is Medium or High, suggest practical improvements that would strengthen the contract.\n"
    "3. Never invent information that is not supported by the contract.\n"
    "4. Keep recommendations concise and actionable.\n\n"

    "Analyze these sections in order:\n\n"

    "1. Confidentiality\n"
    "- Risk Level\n"
    "- Explanation\n"
    "- Recommendation\n\n"

    "2. Liability\n"
    "- Risk Level\n"
    "- Explanation\n"
    "- Recommendation\n\n"

    "3. Termination\n"
    "- Risk Level\n"
    "- Explanation\n"
    "- Recommendation\n\n"

    "4. Intellectual Property\n"
    "- Risk Level\n"
    "- Explanation\n"
    "- Recommendation\n\n"

    "5. Governing Law\n"
    "- Risk Level\n"
    "- Explanation\n"
    "- Recommendation\n\n"

    "6. Missing or Ambiguous Clauses\n"
    "- List important clauses that appear to be missing or unclear based ONLY on the provided contract.\n"
    "- Explain why they may be important.\n"
    "- Recommendation\n\n"

    "Keep the report concise, professional, and easy to read."
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