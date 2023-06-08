from flask import Flask, request
import requests
import hmac
import hashlib
import json
import logging
import openai

app = Flask(__name__)

logging.basicConfig(filename="openai_api_errors.log", level=logging.ERROR)

# facebook parameter
fb_verify_token = "your_fb_verify_token"
app_secret = "your_app_secret"
fb_page_access_token = "your_fb_page_access_token"
fb_api_url = "https://graph.facebook.com/v2.6/"
page_id = "your_page_id"

# openai parameter
openai.api_key = "your_openai_api_key"

# chatbot parameter
message_count = 10

# processed message
processed_message_ids = set()


def verify_webhook(req):
    print("verify_webhook running")

    calling_verify_token = req.args.get("hub.verify_token")

    print(f"calling_verify_token : {calling_verify_token}")

    if calling_verify_token == fb_verify_token:
        challenge = req.args.get("hub.challenge")
        return challenge
    else:
        return "incorrect"

@app.route("/webhook", methods=["GET","POST"])
def listen():
    """This is the main function flask uses to 
    listen at the `/webhook` endpoint"""
    if request.method == "GET":
        return verify_webhook(request)

    if request.method == "POST":
        if validate_request(request):
            payload = request.json
            event = payload["entry"][0]["messaging"]
            for x in event:
                if is_user_message(x):
                    text = x["message"]["text"]
                    sender_id = x["sender"]["id"]
                    message_id = x["message"]["mid"]

                    # Prevent processing of duplicate messages
                    if is_duplicate_message(message_id):
                        continue

                    # Fetch conversation history
                    chat_history = get_history_message(sender_id)

                    # Convert the conversation history to chatgpt format
                    messages = convert_to_chatgpt_message(chat_history, text)

                    print("chat history")
                    for message in messages[1:]]:
                        print(f'  {message["role"]}:{message["content"]}')

                    # Generate reply with Chat-GPT
                    reply_message = generate_reply(messages)

                    send_message(sender_id, reply_message)
            return "ok"
        else:
            return "invalid"


def send_message(recipient_id, reply_message):
    """Send a response to Facebook"""

    payload = {
        "message": {
            "text": reply_message
        },
        "recipient": {
            "id": recipient_id
        },
        "notification_type": "regular"
    }
    auth = {
        "access_token": fb_page_access_token
    }
    response = requests.post(
        fb_api_url+"me/messages",
        params=auth,
        json=payload
    )
    return response.json()

def validate_request(request):
    """Validate the incoming request by comparing X-Hub-Signature"""
    try:
        signature = request.headers["X-Hub-Signature-256"]
    except KeyError:
        return False

    elements = signature.split("=")
    signatureHash = elements[1]

    key = bytes(app_secret, 'UTF-8')
    payload = request.get_data()
    parsed_json = json.loads(payload)
    minified_json = json.dumps(parsed_json, separators=(',', ':'))
    expectedHash = hmac.new(key, msg=minified_json.encode('utf-8'), digestmod=hashlib.sha256).hexdigest()

    print("signature hash : " + signatureHash)
    print("expected hash : " + expectedHash)
    
    if(signatureHash != expectedHash):
        return False
    else:
        return True

def is_user_message(message):
    """Check if the message is a message from the user"""
    return (message.get("message") and
            message["message"].get("text") and
            not message["message"].get("is_echo"))

def get_history_message(sender):
    print("get_history_message running")
    url = f"{fb_api_url}{page_id}/conversations/?user_id={sender}&access_token={fb_page_access_token}&fields=messages"
    response = requests.request("GET", url, headers={}, data={})
    chat_history = []
    chat_ids = response.json()["data"][0]["messages"]["data"]
    for chat in chat_ids[:message_count]:
        messages_id = chat["id"]
        created_time = chat["created_time"]
        get_message_response = get_message(messages_id)
        message = get_message_response["message"]
        from_id = get_message_response["from"]["id"]
        chat_history.append({"message":message, "from_id":from_id})
    return chat_history

def get_message(messages_id):
    url = f"{fb_api_url}{messages_id}?access_token={fb_page_access_token}&fields=from,message"
    response = requests.request("GET", url, headers={}, data={})
    return response.json()

def convert_to_chatgpt_message(chat_history, message):

    # Fetch system role
    system_role = get_system_role()

    # Add system role as the first element of messages
    messages = [{"role": "system", "content": system_role}]

    for chat in chat_history[::-1]:
        role = "user"
        if chat["from_id"]==page_id:
            role = "assistant"
        content  = chat["message"]
        messages.append({"role":role, "content":content})
    messages[-1]={"role":"user", "content":"Answer polite and concisely in a single sentence : "+ message}
    return messages

def generate_reply(messages):

    response_message = "please try again later"

    try:
        print("generate_reply running")

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

    except openai.error.AuthenticationError:
        logging.error("AuthenticationError: Invalid API key.")
    except openai.error.InvalidRequestError:
        logging.error("InvalidRequestError: Invalid API request.")
    except openai.error.RateLimitError:
        logging.error("RateLimitError: API request limit exceeded.")
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")

    return response_message 

def get_system_role():
    with open('system_role.txt', 'r') as file:
        return file.read().strip()
    
def is_duplicate_message(message_id):
    if message_id in processed_message_ids:
        return True
    processed_message_ids.add(message_id)
    return False