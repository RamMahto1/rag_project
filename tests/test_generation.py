from rag_project.components.generation import Generation


question = "How many days of annual leave do employees receive?"

context = """
Employees receive 20 days of annual leave per year.
"""


generation = Generation()

answer = generation.generate_answer(
    question=question,
    context=context
)

print("Question:")
print(question)

print("\nAnswer:")
print(answer)