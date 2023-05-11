# Models: Embedding Models

The last type of models we'll look at are embedding models.

Embedding models take a piece of text and turn it into a vector.

The vector stores semantic information about the text and allows us to do powerful things like semantic search over embedded text.

## Section 1: Initialize An Embedding Model

### Run Commands

Use these to run the files in your `shell`:

**Your Code**

```
python3 your_code/embeddings/01.py
```

**Tutorial Code**

```
python3 tutorial_code/embeddings/01.py
```

### Tutorial

Let's try embedding some text with OpenAI embeddings.

1st we import the OpenAIEmbeddings class and initialize an embedding model.

```python
from langchain.embeddings import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()
```

We can print it to see the model.

```python
print(embeddings)
```

### Full File Code

```python
from langchain.embeddings import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()
```

## Section 2: Embedding A Query

### Run Commands

Use these to run the files in your `shell`:

**Your Code**

```
python3 your_code/embeddings/02.py
```

**Tutorial Code**

```
python3 tutorial_code/embeddings/02.py
```

### Tutorial

Now we can embed our text.

Let's try embeddings a simple example query.

```python
text = 'My favorite food is pizza.'

query_embedding = embeddings.embed_query(text)

print(query_embedding)
```

### Full File Code

```python
from langchain.embeddings import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()

text = 'My favorite food is pizza.'

query_embedding = embeddings.embed_query(text)

print(query_embedding)
```

## Section 3: Embedding Multiple Documents

### Run Commands

Use these to run the files in your `shell`:

**Your Code**

```
python3 your_code/embeddings/03.py
```

**Tutorial Code**

```
python3 tutorial_code/embeddings/03.py
```

### Tutorial

You'll notice we get back a giant list of numbers.

This is a vector!

In OpenAI's case, it's 1536?? numbers that represent the semantic meaning of our text.

We can also embed multiple pieces of text at once with embed_documents.

```python
text1 = 'My favorite food is pizza.'
text2 = 'My favorite food is tacos.'
text3 = 'My favorite food is ice cream.'

document_embeddings = embeddings.embed_documents([text1, text2, text3])

print(len(document_embeddings))
```

### Full File Code

```python
from langchain.embeddings import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()

text1 = 'My favorite food is pizza.'
text2 = 'My favorite food is tacos.'
text3 = 'My favorite food is ice cream.'

document_embeddings = embeddings.embed_documents([text1, text2, text3])

print(len(document_embeddings))
```