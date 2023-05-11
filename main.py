from langchain.llms import OpenAI
import os
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, AIMessage, HumanMessage
from langchain.embeddings import OpenAIEmbeddings

# my_openai_api_key = os.environ['OPENAI_API_KEY']

# llm = OpenAI(model_name="text-curie-001")

# result = llm("Write a poem.")

# print(result)

# num_tokens = llm.get_num_tokens("I am writing Python code!")
# print("Num tokens:", num_tokens)

# llm = OpenAI(streaming=True, callbacks=[StreamingStdOutCallbackHandler()], temperature=1)
# print(llm("Tell me a joke about dogs."))

# chat = ChatOpenAI(temperature=0.5)
# result = chat([SystemMessage(content="Tell the user 3 facts about the Pacific Ocean.")])
# print(result)

# chat = ChatOpenAI(temperature=0.5)
# result = chat([
#     SystemMessage(content="Tell the user 3 facts about the Pacific Ocean."),
#     HumanMessage(content="I am an expert about oceans, so make sure to tell me something I won't know."),
#     AIMessage(content="Okay. I will tell you a super niche fact!")
# ])
# print(result)

# chat = ChatOpenAI(temperature=0.5)

# result = chat.generate([[
#     SystemMessage(content="Tell the user 3 facts about the Pacific Ocean."),
#     HumanMessage(content="I am an expert about oceans, so make sure to tell me something I won't know."),
#     AIMessage(content="Okay. I will tell you a super niche fact!")
# ]] * 2)

# print(len(result.generations))


