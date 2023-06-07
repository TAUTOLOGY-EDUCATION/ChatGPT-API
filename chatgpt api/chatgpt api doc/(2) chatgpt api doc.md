# ChatGPT API Documentation

## **Contents**

- [Completion](#1-completion)
- [Chat](#2-chat)
- [Edit](#3-edit)

## **1. Completion**

### **1.1. How to Use (Python Library)**

The `Completion.create()` method in the OpenAI library allows you to utilize the functionality of the Completion API. Here's a basic usage example:

```python
import openai
openai.api_key = "<your_open_api_key>"

openai.Completion.create(
    model="text-davinci-003",
    prompt="Say this is a test",
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
)
```

The parameters of the `Completion.create()` method are as follows:

- `model` (string, Required): ID of the model to be used. The following models are supported by the Completion API:
    - text-davinci-003
    - text-davinci-002
    - text-curie-001
    - text-babbage-001
    - text-ada-001

- `prompt` (string/array, Optional, Defaults to null): The prompt(s) for generating completions.

- `suffix` (string, Optional, Defaults to null): Suffix after completion of inserted text.

- `max_tokens` (integer, Optional, Defaults to 16): Max tokens to generate in completion.

- `temperature` (number, Optional, Defaults to 1): Sampling temperature, between 0 and 2, for randomness control.

- `top_p` (number, Optional, Defaults to 1): Nucleus sampling parameter.

- `n` (integer, Optional, Defaults to 1): Number of completions to generate for each prompt.

- `stream` (boolean, Optional, Defaults to false): For streaming back partial progress.

- `logprobs` (integer, Optional, Defaults to null): For including the log probabilities on the most likely tokens.

- `echo` (boolean, Optional, Defaults to false): Echo back the prompt in addition to the completion.

- `stop` (string/array, Optional, Defaults to null): Sequences where the API will stop generating tokens.

- `presence_penalty` (number, Optional, Defaults to 0): Penalty for new tokens based on their appearance in the text.

- `frequency_penalty` (number, Optional, Defaults to 0): Penalty for new tokens based on their existing frequency.

- `best_of` (integer, Optional, Defaults to 1): Generates best completions server-side and returns the best one.

- `logit_bias` (map, Optional, Defaults to null): Modify the likelihood of specified tokens appearing in the completion.

- `user` (string, Optional): A unique identifier representing the end-user.

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

### **1.3. Ending Handling**

When using the Completion API, it's essential to manage and handle different ending reasons to ensure the appropriate continuation of the text generation.

The `finish_reason` can be either `stop` or `length`. If the `finish_reason` is `length`, it means that the text generation was ended by reaching the maximum token limit. In this case, you might want to call the completion API again to continue the text generation.

Here is an example of how you can do it:

```python
import openai
openai.api_key = "<your_open_api_key>"

prompt = "Hello world"
response = openai.Completion.create(
    prompt=prompt,
    max_tokens=10,
    model="text-davinci-003",
)

print(f"response:{response.choices[0].text}")

if response.choices[0].finish_reason == "length":
    # Append the generated text to the prompt
    new_prompt = prompt + response.choices[0].text
    # Create a new request with the new prompt
    new_response = openai.Completion.create(prompt=new_prompt, model="text-davinci-003")

    print(f"new_response:{new_response.choices[0].text}")
```

## **2. Chat**

### **2.1. How to Use (Python Library)**

```python
import openai
openai.api_key = "<your_open_api_key>"

openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Who won the football world cup in 2014?"},
        {"role": "assistant", "content": "Germany won the football world cup in 2014."},
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

- `model` (string, Required): The ID of the model used. Refer to the model endpoint compatibility table for model details. The following models are supported by the ChatCompletion API:
    - gpt-4
    - gpt-4-0314
    - gpt-4-32k
    - gpt-4-32k-0314
    - gpt-3.5-turbo
    - gpt-3.5-turbo-0301

- `messages` (array, Required): An array listing the conversation history.

    - `role` (string, Required): The author's role for this message. Possible values include 'system', 'user', or 'assistant'.

    - `content` (string, Required): The content of the message.

    - `name` (string, Optional): The author's name of this message. Acceptable characters include a-z, A-Z, 0-9, and underscores. Maximum length is 64 characters.

- `temperature` (number, Optional, Defaults to 1): Sampling temperature between 0 and 2 for randomness control. Modify this or 'top_p', but not both.

- `top_p` (number, Optional, Defaults to 1): Parameter for nucleus sampling. The model considers tokens with top_p probability mass. Modify this or 'temperature', but not both.

- `n` (integer, Optional, Defaults to 1): The number of chat completion choices generated for each input message.

- `stream` (boolean, Optional, Defaults to false): If set, partial message deltas will be sent, similar to ChatGPT. Tokens will be sent as data-only server-sent events as they become available.

- `stop` (string/array, Optional, Defaults to null): Defines up to 4 sequences where the API will stop generating further tokens.

- `max_tokens` (integer, Optional, Defaults to inf): The maximum number of tokens to generate in the chat completion. The total length of input tokens and generated tokens is limited by the model's context length.

- `presence_penalty` (number, Optional, Defaults to 0): A penalty between -2.0 and 2.0 for new tokens based on their appearance in the text.

- `frequency_penalty` (number, Optional, Defaults to 0): A penalty between -2.0 and 2.0 for new tokens based on their existing frequency.

- `logit_bias` (map, Optional, Defaults to null): Adjusts the likelihood of specific tokens appearing in the completion. Accepts a json object mapping tokens (by their token ID in the tokenizer) to a bias value from -100 to 100.

- `user` (string, Optional): A unique identifier representing the end-user. This can help OpenAI to monitor and detect abuse.

### **2.2. Result Explanation**

The API response will contain the following fields:

```json
{
    "id": "chatcmpl-123",
    "object": "chat.completion",
    "created": 1677652288,
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "The 2014 FIFA World Cup was held in Brazil."
            },
            "finish_reason": "stop"
        }
    ],
    "usage": {
        "prompt_tokens": 9,
        "completion_tokens": 12,
        "total_tokens": 21
    }
}
```

* `id` (string): A unique identifier for the completion.

* `object` (string): The type of object returned, in this case, "chat.completion".

* `created` (integer): A timestamp of when the completion was created.

* `choices` (array): The generated completions, including the generated text, the index of the completion, and the reason why the model stopped generating.

    * `index` (integer): The index of the completion. When you set `n` to more than 1, the API will return multiple completions. The index helps identify each distinct completion.

    * `message` (object): The message object that includes the 'role' and 'content'. The 'role' can be either 'system', 'user', or 'assistant', and 'content' is the actual content of the message.

    * `finish_reason` (string): This indicates why the model stopped generating additional tokens. Possible values are:

        * `stop`: The model reached a token that you specified in the `stop` parameter.

        * `length`: The model reached the maximum token limit you set with the `max_tokens` parameter.

* `usage` (object): Information about the number of tokens used in the API call, including the number of tokens in the prompt, the number of tokens in the completion, and the total number of tokens used.

### **2.3. Ending Handling**

Just like with the Completion API, the `finish_reason` in the chat model response can be `stop` or `length`. If the `finish_reason` is `length`, this means that the chat was cut off because it reached the maximum token limit.

In this case, you might want to call the chat API again to continue the conversation. Here is how you can do it:

```python
import openai
openai.api_key = "<your_open_api_key>"

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    max_tokens=10,
    messages=messages,
)

response_text = response["choices"][0]["message"]["content"]
print(f"response:{response_text}")

if response["choices"][0]["finish_reason"] == "length":
    # Append the last assistant message to the messages
    new_message_assistant = {
        "role": "assistant",
        "content": response["choices"][0]["message"]["content"],
    }
    messages.append(new_message_assistant)
    # Append a new user message to the messages
    new_message_user = {"role": "user", "content": "go on"}
    messages.append(new_message_user)
    # Create a new request with the new messages
    new_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )

    new_response_text = new_response["choices"][0]["message"]["content"]
    print(f"new_response:{new_response_text}")
```

By managing and handling the `finish_reason` effectively, you can control the text and chat generation more effectively and ensure a seamless continuation even when the maximum token limit is reached.

## **3. Edit**

### **3.1. How to Use (Python Library)**

The `Edit.create()` method in the OpenAI library allows you to utilize the functionality of the Edit API. Here's a basic usage example:

```python
import openai
openai.api_key = "<your_open_api_key>"

openai.Edit.create(
    model="text-davinci-edit-001",
    input="What day of the wek is it?",
    instruction="Fix the spelling mistakes"
)
```

The parameters of the `Edit.create()` method are as follows:

* `model` (string, required): The ID of the model to use, which specifies the version and size of the model used. The following models are supported by the Edit API: 

    - text-davinci-edit-001, 
    - code-davinci-edit-001

- `input` (string, Optional, Defaults to ''): The initial text that serves as a starting point for the edit.

- `instruction` (string, Required): The directive that instructs the model how to modify the input text.

- `n` (integer, Optional, Defaults to 1): The number of edits to produce for the input and instruction.

- `temperature` (number, Optional, Defaults to 1): Sampling temperature between 0 and 2. Higher values (like 0.8) result in more random output, whereas lower values (like 0.2) make the output more focused and deterministic. It's recommended to alter this or 'top_p', but not both.

- `top_p` (number, Optional, Defaults to 1): Parameter for nucleus sampling. The model considers tokens with top_p probability mass. For example, 0.1 means only the tokens comprising the top 10% probability mass are considered. It's recommended to alter this or 'temperature', but not both.

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

* `choices` (array): The generated edits, which include the edited text and the index of the edit.
    
    * `index` (integer): The index of the edit. When you set `n` to more than 1, the API will return multiple edits. The index helps identify each distinct edit.
    
    * `text` (string): The edited text.

* `usage` (object): Information about the number of tokens used in the API call, including the number of tokens in the prompt, the number of tokens in the edited text, and the total number of tokens used.