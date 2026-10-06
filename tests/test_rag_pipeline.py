from rag_project.rag_pipeline import RAGPipeline


pipeline = RAGPipeline()


question = "How many days of annual leave do employees receive?"


answer = pipeline.ask(question)


print("Question:")
print(question)

print("\nRAG Answer:")
print(answer)