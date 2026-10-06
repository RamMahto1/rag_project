import chromadb


class VectorStore:

    def __init__(self):
        self.client = chromadb.PersistentClient(
            path="chroma_db"
        )

        self.collection = self.client.get_or_create_collection(
            name="company_policy"
        )

    def add_documents(self, documents, embeddings):
        ids = [str(i) for i in range(len(documents))]

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings
        )

    def search(self, query_embedding, top_k=3):
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        return results