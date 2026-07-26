import faiss
import numpy as np
import os
import pickle


def create_vector_store(embeddings):
    dimension = embeddings.shape[1]#dimention = 384

    index = faiss.IndexFlatL2(dimension)#creates Empty database that stores index of vecotrs vectors of length 384.


    index.add(np.array(embeddings).astype("float32"))

    return index


def search(index, query_embedding, k=3):
    distances, indices = index.search(
        np.array(query_embedding).astype("float32"), #by default it's float64 but faiss only works on 32
        k
    )

    return indices

#The index of chunk in chunks list matches the index of the vector in FAISS.
#That's how we know which text belongs to which embedding.

#do this with langchain later. 

def save_vector_store(index, chunks, subject):
    folder = os.path.join("vector_store", subject)
    os.makedirs(folder, exist_ok=True)

    faiss.write_index(index, os.path.join(folder, "index.faiss"))

    with open(os.path.join(folder, "chunks.pkl"), "wb") as f:
        pickle.dump(chunks, f)


def load_vector_store(subject):
    folder = os.path.join("vector_store", subject)

    index = faiss.read_index(os.path.join(folder, "index.faiss"))

    with open(os.path.join(folder, "chunks.pkl"), "rb") as f:
        chunks = pickle.load(f)

    return index, chunks