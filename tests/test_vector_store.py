from rag_project.components.data_ingestion import DataIngestion
from rag_project.components.data_chunking import DataChunking
from rag_project.components.embedding import Embedding
from rag_project.components.vector_store import VectorStore


data_path = "documents/company_policy.txt"

ingestion = DataIngestion(data_path)
text = ingestion.load_document()


chunking = DataChunking(
    chunk_size=100,
    overlap=20
)

chunks = chunking.split_text(text)


embedding = Embedding()

embeddings = []

for chunk in chunks:
    vector = embedding.create_embedding(chunk)
    embeddings.append(vector)


vector_store = VectorStore()

vector_store.add_documents(
    documents=chunks,
    embeddings=embeddings
)


print("Vector database created successfully")
print("Number of chunks stored:", len(chunks))
print("Vector store test started")