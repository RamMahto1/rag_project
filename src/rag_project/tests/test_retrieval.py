from rag_project.components.embedding import Embedding
from rag_project.components.vector_store import VectorStore


# User question
query = "How many days of annual leave do employees receive?"


# Create query embedding
embedding = Embedding()

query_vector = embedding.create_embedding(query)


# Search vector database
vector_store = VectorStore()

results = vector_store.search(
    query_embedding=query_vector,
    top_k=3
)


# Display retrieved chunks
print("Retrieved chunks:")

for i, document in enumerate(results["documents"][0], start=1):
    print(f"\n--- Result {i} ---")
    print(document)