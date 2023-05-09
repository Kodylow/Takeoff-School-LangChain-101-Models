from langchain.llms import OpenAI

llm = OpenAI(model_name="text-curie-001")

result = llm("Write a poem.")

print(result)