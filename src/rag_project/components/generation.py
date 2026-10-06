from openai import OpenAI

from rag_project.rag_config import RAGConfig


class Generation:

    def __init__(self):
        self.client = OpenAI(
            api_key=RAGConfig.OPENAI_API_KEY
        )

    def generate_answer(self, question: str, context: str):

        prompt = f"""
Answer the question using only the provided context.

Context:
{context}

Question:
{question}

Answer:
"""

        response = self.client.responses.create(
            model="gpt-5-mini",
            input=prompt
        )

        return response.output_text