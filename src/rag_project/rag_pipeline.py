from rag_project.components.embedding import Embedding
from rag_project.components.vector_store import VectorStore
from rag_project.components.context_builder import ContextBuilder
from rag_project.components.generation import Generation


class RAGPipeline:

    def __init__(self):

        self.embedding = Embedding()
        self.vector_store = VectorStore()
        self.context_builder = ContextBuilder()
        self.generation = Generation()

    def ask(self, question: str):

        query_vector = self.embedding.create_embedding(question)

        results = self.vector_store.search(
            query_embedding=query_vector,
            top_k=3
        )

        documents = results["documents"][0]

        context = self.context_builder.build_context(documents)

        answer = self.generation.generate_answer(
            question=question,
            context=context
        )

        return answer