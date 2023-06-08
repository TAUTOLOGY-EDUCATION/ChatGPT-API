# Enhance Your Chatbot with Chat-GPT

You can significantly improve the interaction quality of your chatbot by integrating the OpenAI's Chat-GPT model. This powerful AI model enables your chatbot to generate human-like responses.

The existing Facebook chatbot server code needs some adjustments to incorporate the Chat-GPT model. This document explains the steps needed to edit your "server.py" file for the Facebook chatbot.

Let's get started!

## Workflow Sequence Diagram

Below is the sequence diagram that represents the workflow of the enhanced chatbot:

![sequence diagram](chatgpt_enhance.svg)

## Adding Chat History

First, we will add the functionality to get the conversation history. This history can then be used as input for the Chat-GPT model. Add the following functions to your "server.py" file.

```python
def get_history_message(sender):
    print("get_history_message running")
    url = f"{fb_api_url}{page_id}/conversations/?user_id={sender}&access_token={fb_page_access_token}&fields=messages"
    response = requests.request("GET", url, headers={}, data={})
    chat_history = []
    chat_ids = response.json()["data"][0]["messages"]["data"]
    for chat in chat_ids[:message_count]:
        messages_id = chat["id"]
        created_time = chat["created_time"]
        if is_old_message(created_time):
            break
        get_message_response = get_message(messages_id)
        message = get_message_response["message"]
        from_id = get_message_response["from"]["id"]
        chat_history.append({"message":message, "from_id":from_id})
    return chat_history

def get_message(messages_id):
    url = f"{fb_api_url}{messages_id}?access_token={fb_page_access_token}&fields=from,message"
    response = requests.request("GET", url, headers={}, data={})
    return response.json()
```

These functions will call Facebook API to retrieve chat history between the user and your page.

## Adding Chat-GPT for Reply Generation

Next, we will use the `chat()` method provided by the OpenAI API for generating the reply message. Here is the function:

```python
def generate_reply(messages):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.2,
            top_p=0.2,
            max_tokens=512,
        )
        
        response_message = response.choices[0].message.content
        finish_reason = response.choices[0].finish_reason

        if finish_reason == "length":
            response_message = response_message+"..."

    except ex:
        logging.error(f"Unexpected error: {str(e)}")
        response_message = "please try again later"

return response_message 
```

This function generates a reply message using the Chat-GPT model. If the reason for the termination of the message is the length, the response is appended with "..." to indicate the message was cut off. 

## Integrating into Existing Server Code

Lastly, we will integrate the functions into the existing server code. In the `listen()` function, call `get_history_message()` to get the chat history and pass it to `generate_reply()` for generating the reply.

Replace the line:
```python
reply_message = f"reply for:{text}"
```
with the following lines:
```python
history = get_history_message(sender_id)
reply_message = generate_reply(history)
```

That's it! With these adjustments, your chatbot can generate much more intelligent responses using the power of OpenAI's Chat-GPT.

In the provided Python code, there are a few parameters that are currently hard-coded and can be defined globally for better code organization. Here's how you can define them at the top of your "server.py" script:

```python
# Facebook parameters
fb_api_url = "https://graph.facebook.com/v2.6/"
fb_page_access_token = "your_page_access_token"
page_id = "your_page_id"
app_secret = "your_app_secret"
fb_verify_token = "your_fb_verify_token" # Please replace with your Facebook verify token

# Message parameters
message_count = 5 # Define how many previous messages to retrieve
```

Note: Make sure to replace `your_page_id` with your actual Facebook page ID and `your_fb_verify_token` with your actual Facebook verify token.

Also, the `message_count` parameter defines how many past messages you want to consider for generating the reply. Adjust it according to your requirements. 

Remember to update the respective places in your code where these values are used with the corresponding variable names.