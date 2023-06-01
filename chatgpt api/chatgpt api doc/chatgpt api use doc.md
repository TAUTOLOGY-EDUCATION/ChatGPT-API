# ChatGPT API Documentation

**Last updated: June 1, 2023**

## **Contents**

- [Completion](#1-completion)
- [Chat](#2-chat)
- [Edit](#3-edit)

## **1. Completion**

### **1.1. How to Use (Python Library)**

The `Completion.create()` method in the OpenAI library allows you to utilize the functionality of the Completion API. Here's a basic usage example:

```python
import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Completion.create(
    model="text-davinci-003",
    prompt="your prompt",
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=["stop_word_1", "stop_word_2"]
)
```

The parameters of the `Completion.create()` method are as follows:

* `model` (string, required): The ID of the model to use, which specifies the version and size of the model used. The following models are supported by the Completion API:
    * text-davinci-003
    * text-davinci-002
    * text-curie-001
    * text-babbage-001
    * text-ada-001
* `prompt` (string, required): The initial text to be extended or completed.
* `max_tokens` (integer, optional): The maximum length of the generated text. If not provided, the model will decide the number of tokens to generate.
* `temperature` (float, optional): This controls the randomness of the model's output. Higher values result in more random outputs.
* `top_p` (float, optional): This controls the nucleus sampling, which selects the next token from the top p% of the probability distribution.
* `frequency_penalty` (float, optional): This penalizes new tokens based on their frequency of occurrence. The value can range from -2 to 2, with negative values favoring less common tokens, and positive values favoring more common ones.
* `presence_penalty` (float, optional): This penalizes new tokens based on whether they are novel in the given context. The value can range from -2 to 2, with negative values favoring the use of new tokens, and positive values favoring existing ones.
* `stop` (array of strings, optional): This is a list of tokens that will make the model stop generating further tokens.

### **1.2. Result Explanation**

The API response will contain the following fields:

```json
{
    "id": "cmpl-uqkvlQyYK7bGYrRHQ0eXlWi7",
    "object": "text_completion",
    "created": 1589478378,
    "model": "text-davinci-003",
    "choices": [
        {
            "text": "\n\nThis is indeed a test",
            "index": 0,
            "logprobs": null,
            "finish_reason": "length"
        }
    ],
    "usage": {
        "prompt_tokens": 5,
        "completion_tokens": 7,
        "total_tokens": 12
    }
}
```

* `id` (string): A unique identifier for the completion.
* `object` (string): The type of object returned, in this case, "text_completion".
* `created` (integer): A timestamp of when the completion was created.
* `model` (string): The ID of the model used for this completion.
* `choices` (array): The generated completions. It includes the generated text, the index of the completion, the log probabilities, and the reason why the model stopped generating.
    * `text` (string): The generated completion. This is the text that the model has generated as a completion of your prompt.
    * `index` (integer): The index of the completion. When you set `n` to more than 1, the API will return multiple completions. The index helps identify each distinct completion.
    * `logprobs` (object or null): If you have set the `logprobs` parameter in your request, this will be an object showing the log probabilities of the tokens generated. Otherwise, it will be null.
    * `finish_reason` (string): This indicates why the model stopped generating additional tokens. Possible values are:
        * `stop`: The model reached a token that you specified in the `stop` parameter.
        * `length`: The model reached the maximum token limit you set with the `max_tokens` parameter.
* `usage` (object): Information about the number of tokens used in the API call, including the number of tokens in the prompt, the number of tokens in the completion, and the total number of tokens used.

### **1.3. Error Handling**

If your API request triggers an error, the response will contain an `error` object with more details. For example:

```json
{
    "error": {
        "code": "validation_error",
        "message": "max_tokens parameter is too high. Value must be less than or equal to 4096.",
        "param": "max_tokens"
    }
}
```

* `code` (string): A short, machine-readable string that specifies the type of error.
* `message` (string): A human-readable string detailing the error.
* `param` (string, optional): If the error relates to a specific parameter in the request, this field will mention that parameter's name.

Sure, I can help you complete the missing sections in your document.

## **2. Chat**

### **2.1. How to Use (Python Library)**

```python
import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Who won the football world cup in 2014?"},
        {
            "role": "assistant",
            "content": "Germany won the football world cup in 2014.",
        },
        {"role": "user", "content": "Where was it played?"},
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
)
```

The parameters of the `ChatCompletion.create()` method are as follows:

* `model` (string, required): The ID of the model to use, which specifies the version and size of the model used. The following models are supported by the ChatCompletion API:
    * gpt-4
    * gpt-4-0314
    * gpt-4-32k
    * gpt-4-32k-0314
    * gpt-3.5-turbo
    * gpt-3.5-turbo-0301

* `messages` (array, required): An array of message objects. Each object should have a role (either "system", "user", or "assistant") and content (the content of the message). The messages must be passed in the order they occurred.

* `temperature` (float, optional): Controls the randomness of the model's output. Higher values result in more random outputs.

* `max_tokens` (integer, optional): The maximum length of the generated text. If not provided, the model will decide how many tokens to generate.

* `top_p` (float, optional): Controls the nucleus sampling, which chooses the next token from the top p% of the probability distribution.

* `frequency_penalty` (float, optional): Penalizes new tokens based on their frequency of occurrence. The value can range from -2 to 2, with negative values increasing the frequency of less common tokens, and positive values decreasing it.

* `presence_penalty` (float, optional): Penalizes new tokens based on whether they are novel in the given context or not. The value can range from -2 to 2, with negative values making the model more likely to use new tokens, and positive values making it more likely to use existing tokens.

### **2.2. Result Explanation**

The API response will contain the following fields:

```json
    {
      "id": "chatcmpl-123",
      "object": "chat.completion",
      "created": 1677652288,
      "choices": [{
        "index": 0,
        "message": {
          "role": "assistant",
          "content": "\n\nHello there, how may I assist you today?",
        },
        "finish_reason": "stop"
      }],
      "usage": {
        "prompt_tokens": 9,
        "completion_tokens": 12,
        "total_tokens": 21
      }
    }
```

* `id` (string): A unique identifier for the completion.
* `object` (string): The type of object returned, in this case, "chat

.completion".
* `created` (integer): A timestamp of when the completion was created.
* `choices` (array): The generated completions, including the generated text, the index of the completion, and the reason why the model stopped generating.
    * `index` (integer): The index of the completion. When you set `n` to more than 1, the API will return multiple completions. The index helps identify each distinct completion.
    * `message` (object): The message object that includes the 'role' and 'content'. The 'role' can be either 'system', 'user', or 'assistant', and 'content' is the actual content of the message.
    * `finish_reason` (string): This indicates why the model stopped generating additional tokens. Possible values are:
        * `stop`: The model reached a token that you specified in the `stop` parameter.
        * `length`: The model reached the maximum token limit you set with the `max_tokens` parameter.
* `usage` (object): Information about the number of tokens used in the API call, including the number of tokens in the prompt, the number of tokens in the completion, and the total number of tokens used.

## **3. Edit**

### **3.1. How to Use (Python Library)**

```python
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Edit.create(
  model="text-davinci-edit-001",
  input="prompt",
  instruction="instruction",
  temperature=1,
  top_p=1
)
```

The parameters of the `Edit.create()` method are as follows:

* `model` (string, required): The ID of the model to use, which specifies the version and size of the model used. The following models are supported by the Edit API: 
    * text-davinci-edit-001, 
    * code-davinci-edit-001

* `input` (string, required): The text to be edited.

* `instruction` (string, required): The direction to guide the model's editing process. For example, "correct grammar and spelling" or "condense the text".

* `temperature` (float, optional): Controls the randomness of the model's output. Higher values result in more random outputs.

* `top_p` (float, optional): Controls the nucleus sampling, which chooses the next token from the top p% of the probability distribution.

### **3.2. Result Explanation**

The API response will contain the following fields:

```json
    {
        "object": "edit",
        "created": 1589478378,
        "choices": [
            {
            "text": "What day of the week is it?",
            "index": 0,
            }
        ],
        "usage": {
            "prompt_tokens": 25,
            "completion_tokens": 32,
            "total_tokens": 57
        }
    }
```

* `object` (string): The type of object returned, in this case, "edit".
* `created` (integer): A timestamp of when the edit was created.
* `choices` (array): The generated edits, including the edited text and the index of the edit.
    * `index` (integer): The index of the edit. When you set `n` to more than 1, the API will return multiple edits. The index helps identify each distinct edit.
    * `text` (string): The edited text.
* `usage` (object): Information about the number of tokens used in the API call, including the number of tokens in the input, the number of tokens in the edited text, and the total number of tokens used.