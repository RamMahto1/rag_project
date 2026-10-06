from rag_project.components.context_builder import ContextBuilder


documents = [
    "Employees receive 20 days of annual leave.",
    "Employees can work remotely up to 2 days per week.",
    "Performance is reviewed twice a year."
]


context_builder = ContextBuilder()

context = context_builder.build_context(documents)

print("Context:")
print(context)