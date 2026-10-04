from rag_project.components.data_ingestion import DataIngestion
from rag_project.components.data_chunking import DataChunking

data_path = "documents/company_policy.txt"

ingestion = DataIngestion(data_path)
text = ingestion.load_document()

chunking = DataChunking(
    chunk_size=100,
    overlap=20
)

chunks = chunking.split_text(text)

for i, chunk in enumerate(chunks, start=1):
    print(f"\n--- Chunk {i} ---")
    print(chunk)