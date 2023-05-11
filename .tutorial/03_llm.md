# Models: LLMs

## Section 1: Making A Request

### Run Commands

Use these to run the files in your `shell`:

**Your Code**

```
python3 your_code/llm/01.py
```

**Tutorial Code**

```
python3 tutorial_code/llm/01.py
```

### Tutorial

Let's start with standard LLMs.

We're going to import the the OpenAI LLM wrapper to get started.

This wrapper extends the base LLM class from LangChain.

It gives us a simple interface to hook into OpenAI's LLMs.

```python
from langchain.llms import OpenAI
```

Now we're going to initialize an LLM with the wrapper.

Here we create a new variable llm and assign it to an OpenAI LLM with the specified parameters.

We'll test it with the text-curie-001 model.

```python
llm = OpenAI(model_name="text-curie-001")
```

Let's try making a call with our llm!

We'll pass in a string to the llm, and we'll get back the result as a string.

```python
llm("Write a poem.")
```

### Full File Code

```python
from langchain.llms import OpenAI

llm = OpenAI(model_name="text-curie-001")

result = llm("Write a poem.")

print(result)
```

## Section 2: Using Generate

### Run Commands

Use these to run the files in your `shell`:

**Your Code**

```
python3 your_code/llm/02.py
```

**Tutorial Code**

```
python3 tutorial_code/llm/02.py
```

### Tutorial

The LLM class comes with all sorts of useful functionality.

Another thing we can do is use the `generate` method.

Let's try passing in 2 strings to the generate function as a list. This will make 2 requests instead of just 1.

We'll save the generations to `result`.

```python
result = llm.generate(["Write a poem about fire.", "Write a poem about water."])
```

Now let's print out our fire poem.

```python
print(result.generations[0][0].text)
```

Nice! We got a fire poem just like we asked for.

We can also access helpful information like token usage.

```python
print(result.llm_output)
```

### Full File Code

```python
from langchain.llms import OpenAI

llm = OpenAI(model_name="text-curie-001")

result = llm.generate(["Write a poem about fire.", "Write a poem about water."])

print(result.generations[0][0].text)
print("\n")
print(result.llm_output)
```

## Section 3: Token Usage

### Run Commands

Use these to run the files in your `shell`:

**Your Code**

```
python3 your_code/llm/03.py
```

**Tutorial Code**

```
python3 tutorial_code/llm/03.py
```

### Tutorial

LangChain also provides some helpful ways to estimate token usage.

As of writing this, only OpenAI LLMs support token tracking in LangChain.

For reference, tiktoken is the default tokenizer.

Let's install it. Run this in your `shell`:

```
pip install tiktoken
```

Here we check how many tokens this sentence uses.

```python
llm.get_num_tokens("I am writing Python code!")
```

### Full File Code

```python
from langchain.llms import OpenAI

llm = OpenAI(model_name="text-curie-001")

token_count = llm.get_num_tokens("I am writing Python code!")

print(token_count)
```

## Section 4: Streaming

### Run Commands

Use these to run the files in your `shell`:

**Your Code**

```
python3 your_code/llm/04.py
```

**Tutorial Code**

```
python3 tutorial_code/llm/04.py
```

### Tutorial

Another helpful tool you'll want to know how to use is streaming.

Streaming allows us to "stream" tokens as they come in from the request.

Let's create a new llm with streaming enabled and ask it to tell us a joke.

This time you'll notice the tokens output as they come in instead of waiting for the entire request to finish.

```python
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

llm = OpenAI(streaming=True, callbacks=[StreamingStdOutCallbackHandler()], temperature=1)
llm("Tell me a joke about dogs.")
```

### Full File Code

```python
from langchain.llms import OpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

llm = OpenAI(streaming=True, callbacks=[StreamingStdOutCallbackHandler()], temperature=1)

result = llm("Tell me a joke about dogs.")
```