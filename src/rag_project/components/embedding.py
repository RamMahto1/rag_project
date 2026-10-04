from openai import OpenAI

from rag_project.rag_config import RAGConfig


class Embedding:

    def __init__(self):
        self.client = OpenAI(
            api_key=RAGConfig.OPENAI_API_KEY
        )

    def create_embedding(self, text: str):
        response = self.client.embeddings.create(
            model="text-embedding-3-small",
            input=text
        )

        return response.data[0].embedding