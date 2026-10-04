from src.rag_project.components.data_ingestion import DataIngestion


data_path = "documents/company_policy.txt"

ingestion = DataIngestion(data_path)

text = ingestion.load_document()

print(text)