from fastapi import APIRouter, UploadFile, File
import os

from app.services.pdf_loader import extract_text
from app.services.chunker import create_chunks
from app.services.embeddings import create_embeddings
from app.services.vector_store import create_vector_store,save_vector_store


router = APIRouter()

UPLOAD_DIR = "uploaded_pdfs"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    #extracting text
    text = extract_text(file_path)

    #making chunks
    chunks = create_chunks(text)

    #creating embeddings for each chunk:
    embeddings = create_embeddings(chunks)

        # Create FAISS index
    vector_store = create_vector_store(embeddings)

    # Get subject name from filename
    subject = os.path.splitext(file.filename)[0]

    # Save to disk
    save_vector_store(vector_store, chunks, subject)

    return {
    "message": "PDF uploaded successfully",
    "subject": subject,
    "total_chunks": len(chunks)
}