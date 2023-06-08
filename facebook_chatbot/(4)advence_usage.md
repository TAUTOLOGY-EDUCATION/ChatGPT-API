# Adding a System Role and Preventing Duplicate Reply Messages

In this guide, we will edit the `server.py` file step by step:

1. Create and read text from `system_role.txt` for use as a system role in the ChatGPT-Chat API.
2. Add a method to prevent duplicate reply messages when the Facebook call webhook is invoked twice.
3. Edit the code to utilize the system role and prevent duplicate messages.

## Step 1: Create and Read System Role from Text File

Let's add a helper function to read the system role from a text file. The function will take the file path as input and return the content as a string.

```python
def get_system_role():
    with open('system_role.txt', 'r') as file:
        return file.read().strip()
```

The text will be read from `system_role.txt` and used as the system role in the chatgpt-chat API.

## Step 2: Add Method to Prevent Duplicate Reply Messages

To prevent duplicate messages when the Facebook call webhook is called twice, we will add a simple caching mechanism. In this cache, we will store the IDs of messages that we have already processed.

Let's add a global set for storing processed message IDs:

```python
processed_message_ids = set()
```

Now, let's add a function to check if a message has already been processed:

```python
def is_duplicate_message(message_id):
    if message_id in processed_message_ids:
        return True
    processed_message_ids.add(message_id)
    return False
```

The `is_duplicate_message` function checks whether a message ID is in the `processed_message_ids` set. If it is, the function returns `True`; otherwise, it adds the message ID to the set and returns `False`.

## Step 3: Modify Code to Use System Role and Prevent Duplicate Messages

Now, let's modify the `listen` function to prevent the processing of duplicate messages.

```python
@app.route("/webhook", methods=["GET","POST"])
def listen():
    # code omitted for brevity...

    if request.method == "POST":
        # code omitted for brevity...
        for x in event:
            if is_user_message(x):
                message_id = x["message"]["mid"]

                # Prevent processing of duplicate messages
                if is_duplicate_message(message_id):
                    continue

                # rest of the code...

    # code omitted for brevity...
```

And modify the `convert_to_chatgpt_message` function to use the system role

```python
def convert_to_chatgpt_message(chat_history, message):

    # Fetch system role
    system_role = get_system_role()

    # Add system role as the first element of messages
    messages = [{"role": "system", "content": system_role}]
    
    # rest of the code...
```

Make sure to replace the `"server.py"` file's content with these modifications. Your Python script should now be able to prevent duplicate reply messages and include the system role from a text file in the conversation with the ChatGPT-Chat API.