 # Setup

## Install

Before we examine each of the 3 types of models, let's install LangChain & OpenAI.

Run this code in your `shell`:

```
pip install langchain openai
```

## Keys

For this course, you're going to need an OpenAI API key.

Get an OpenAI API key [here](https://platform.openai.com/account/api-keys).

Remember - keep this a secret!

Once you have your key, you're going to need to save it as an environment variable.

To do this, you can use Replit's "Secrets" tool. On the left under your file explorer, you'll see a "tools" section. You're going to want to click on the "Secrets" tool. It's the one with the lock icon.

Once in the Secrets Tool, do the following:
- enter "OPENAI_API_KEY" in the "key" input
- enter your OpenAI API Key in the "value" input
- click the "Add new secret" button

This will securely save your key and allow you to access it in your code.

Now close the `shell` tool and reopen it.

Test that this works by hitting the green `run` button.

Your api key should be printing to the console.

If the console complains that you don't have a key set, you probably need to restart the `shell` as mentioned above.