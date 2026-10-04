from rag_project.components.embedding import Embedding


embedding = Embedding()

text = "Employees can work remotely up to 2 days per week."

vector = embedding.create_embedding(text)

print("Embedding created successfully")
print("Vector type:", type(vector))
print("Vector length:", len(vector))
print("First 5 values:", vector[:5])