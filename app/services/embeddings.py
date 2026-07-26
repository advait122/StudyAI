from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2") #downloads the embedding model (only the first time) and loads it into memory


def create_embeddings(chunks: list[str]):
    embeddings = model.encode(chunks)

    return embeddings #returns one embedding vector for each chunk.

def create_query_embedding(query: str):
    embedding = model.encode([query])

    return embedding

#For every chunk, the model produces one vector, and that vector contains 384 numbers.
#384 is default value produced by miniLM
#The embedding model has learned during training how to place text in a 384-dimensional semantic space.