from fastapi import APIRouter

from app.services.embeddings import create_query_embedding
from app.services.vector_store import search, load_vector_store
from app.services.llm import generate_answer

router = APIRouter()


@router.post("/ask")
def ask(question: str, subject: str):
    
    vector_store, chunks = load_vector_store(subject)
    query_embedding = create_query_embedding(question)

    indices = search(vector_store, query_embedding)

    results = []

    for i in indices[0]:
        results.append(chunks[i])

    context = "\n\n".join(results)

    answer = generate_answer(question, context)

    return {
        "question": question,
        "answer": answer
    }