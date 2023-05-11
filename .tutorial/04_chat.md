# Models: Chat Models

Now we move our attention over to Chat Models.

Chat models are just LLMs with a chat-like interface.

Instead of passing a string in and getting a string out, we pass in messages and get a message as a result.

## Section 1: Initializing A Chat Model

### Run Commands

Use these to run the files in your `shell`:

**Your Code**

```
python3 your_code/chat/01.py
```

**Tutorial Code**

```
python3 tutorial_code/chat/01.py
```

### Tutorial

Let's initialize an OpenAI chat model with a temperature of 0.5.

By default this wrapper uses the gpt-3.5-turbo model.

### Full File Code

```python
from langchain.chat_models import ChatOpenAI

chat = ChatOpenAI(temperature=0.5)
```

## Section 2: Making A Request

### Run Commands

Use these to run the files in your `shell`:

**Your Code**

```
python3 your_code/chat/02.py
```

**Tutorial Code**

```
python3 tutorial_code/chat/02.py
```

### Tutorial

To get a completion with this model we need to pass it some messages.

There are 3 types of messages:

System messages.
Human messages.
AI messages.
The system message acts as the instruction for the system.

Here we create a SystemMessage that instructs the model to tell us about the Pacific Ocean.

### Full File Code

```python
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage

chat = ChatOpenAI(temperature=0.5)

result = chat([SystemMessage(content="Tell the user 3 facts about the Pacific Ocean.")])

print(result)
```

## Section 3: A Full Chat

### Run Commands

Use these to run the files in your `shell`:

**Your Code**

```
python3 your_code/chat/03.py
```

**Tutorial Code**

```
python3 tutorial_code/chat/03.py
```

### Tutorial

Sure enough, it tells us 3 facts about the Pacific Ocean.

You'll notice it responds with an AIMessage. This is a message that represents the AI's messages.

Our own messages are defined as a HumanMessage.

We can simulate a conversation history by passing in a few AI and human messages like this.

### Full File Code

```python
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, AIMessage, HumanMessage 

chat = ChatOpenAI(temperature=0.5)

result = chat([
    SystemMessage(content="Tell the user 3 facts about the Pacific Ocean."),
    HumanMessage(content="I am an expert about oceans, so make sure to tell me something I won't know."),
    AIMessage(content="Okay. I will tell you a super niche fact!")
])

print(result)
```

## Section 4: Streaming

### Run Commands

Use these to run the files in your `shell`:

**Your Code**

```
python3 your_code/chat/04.py
```

**Tutorial Code**

```
python3 tutorial_code/chat/04.py
```

### Tutorial

We can also stream the response.

### Full File Code

```python
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, AIMessage, HumanMessage
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

chat = ChatOpenAI(streaming=True, callbacks=[StreamingStdOutCallbackHandler()], temperature=0.5)

result = chat([
    SystemMessage(content="Tell the user 3 facts about the Pacific Ocean."),
    HumanMessage(content="I am an expert about oceans, so make sure to tell me something I won't know."),
    AIMessage(content="Okay. I will tell you a super niche fact!")
])

print(result)
```

## Section 5: Using Generate

### Run Commands

Use these to run the files in your `shell`:

**Your Code**

```
python3 your_code/chat/05.py
```

**Tutorial Code**

```
python3 tutorial_code/chat/05.py
```

### Tutorial

Remember how we batches multiple generations with standard LLMs?

We can do that with chat models too.

Let's get 2 generations with the same chat.

Sure enough, if we print out the length of our generations we have 2 of them.

### Full File Code

```python
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, AIMessage, HumanMessage

chat = ChatOpenAI(temperature=0.5)

result = chat.generate([[
    SystemMessage(content="Tell the user 3 facts about the Pacific Ocean."),
    HumanMessage(content="I am an expert about oceans, so make sure to tell me something I won't know."),
    AIMessage(content="Okay. I will tell you a super niche fact!")
]] * 2)

print(len(result.generations))
```