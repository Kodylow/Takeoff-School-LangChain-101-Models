from langchain.llms import OpenAI
import os
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chat_models import ChatOpenAI

# my_openai_api_key = os.environ['OPENAI_API_KEY']

# llm = OpenAI(model_name="text-curie-001")

# result = llm("Write a poem.")

# print(result)

# num_tokens = llm.get_num_tokens("I am writing Python code!")
# print("Num tokens:", num_tokens)

# llm = OpenAI(streaming=True, callbacks=[StreamingStdOutCallbackHandler()], temperature=1)
# print(llm("Tell me a joke about dogs."))

chat = ChatOpenAI(temperature=0.5)