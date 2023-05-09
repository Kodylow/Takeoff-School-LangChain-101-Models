# Setup

## Install

Before we examine each of the 3 types of models, let's install LangChain & OpenAI.

Run this code in your `shell`:

```
pip install langchain openai
```

## Update

We also need to upgrade pydantic.

```
pip install --upgrade pydantic
```

## Keys

Now go over to `secrets` and add a new environment variable called  `OPENAI_API_KEY`

Test that this works by hitting the green `run` button.

Your api key should be printing to the console.

Remember - keep this a secret!