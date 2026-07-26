import os
from groq import Groq

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_answer(question: str, context: str) -> str:

    prompt = f"""
You are SmartStudyAI, an exam preparation assistant.

Answer ONLY using the provided context.

If the answer is not present in the context, reply:
"I couldn't find this information in the uploaded PDF."

Keep the answer:
- Concise
- Exam-oriented
- Use bullet points when appropriate
- Do not add information that is not present in the context.

Context:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content