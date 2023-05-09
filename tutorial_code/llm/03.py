from langchain.llms import OpenAI

llm = OpenAI(model_name="text-curie-001")

token_count = llm.get_num_tokens("I am writing Python code!")

print(token_count)