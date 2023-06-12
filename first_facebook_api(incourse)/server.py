import requests
from flask import Flask, request
import openai
from datetime import datetime, timedelta

import hmac
import hashlib
import json
import logging

app = Flask(__name__)

app_secret = "98110ea57d51f9afdbb37137763ee68b"
openai.api_key = "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"
fb_page_access_token = "EAACATYzzfZCsBAJJo2OTfQ15tjw4FRQYgKBRE6cJ704aypkTEK2CoZBg17CL3FJphQOcVZCHsfV6cHqyarZBF1ZBCLvSoQ3vcYkmw2qMPGItBBBZAXRJRlWm7Hpt770BZAfsAyu4CCzz9pWAwNb6Td2dZCyiUiHFWkn2GXhMEoVhxcvNaAgDa4xx"
fb_api_url = "https://graph.facebook.com/v2.6/"
page_id = "100791973054202"
message_count = 5
old_day = 3

logging.basicConfig(filename="openai_api_errors.log", level=logging.ERROR)

processed_message_ids = set()

@app.route("/webhook", methods=["GET","POST"])
def listen():
    print(f"Calling webhook method : {request.method}")
    """This is the main function Flask uses to 
    listen at the `/webhook` endpoint"""
    if request.method == "GET":
        return verify_webhook(request)
    if request.method == "POST":

        if validate_request(request):

            payload = request.json

            event = payload["entry"][0]["messaging"]
            for x in event:
                if is_user_message(x):

                    message_id = x["message"]["mid"]

                    if is_processed(message_id):
                        return "ok"

                    text = x["message"]["text"]
                    sender_id = x["sender"]["id"]

                    message_history = get_history_message(sender_id)

                    system_role_txt = get_system_role()

                    message_history_gpt = convert_to_chatgpt_message(message_history, system_role_txt)

                    reply_message = generate_reply(message_history_gpt)

                    send_message(sender_id, reply_message)

                else:
                    print("not user message")    
            return "ok"
        
        else:
            return "invalid"
    
def verify_webhook(req):
    print("verify_webhook running")
    calling_verify_token = req.args.get("hub.verify_token")
    print(f"calling_verify_token : {calling_verify_token}")
    fb_verify_token = "fb_verify_token"
    if calling_verify_token == fb_verify_token:
        challenge = req.args.get("hub.challenge")
        return challenge
    else:
        return "incorrect"
    
def send_message(recipient_id, reply_message):
    """Send a response to Facebook"""
    
    payload = {
        "message": {
            "text": reply_message,
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

    payload = request.get_data()
    parsed_json = json.loads(payload)
    minified_json = json.dumps(parsed_json, separators=(',', ':'))

    key = bytes(app_secret, 'UTF-8')

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

def generate_reply(messages):

    max_tokens = 1000

    print(f"max_tokens:{max_tokens}")

    finish_reason = "stop"
    response_message = "โปรดรอการตอบกลับจากเจ้าหน้าที่"

    try:
        response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0.2,
                top_p=0.2,
                max_tokens=max_tokens,
            )
        
        finish_reason = response["choices"][0]["finish_reason"] 
        response_message = response["choices"][0]["message"]["content"]
    
        print(finish_reason)
        print(response_message)

    except openai.error.AuthenticationError:
        logging.error("AuthenticationError: Invalid API key.")
        print(
            "There was a problem with your authentication. Please check your API key."
        )
    except openai.error.InvalidRequestError:
        logging.error("InvalidRequestError: Invalid API request.")
        print("You made an invalid request. Please check the provided parameters.")
    except openai.error.RateLimitError:
        logging.error("RateLimitError: API request limit exceeded.")
        print(
            "You've exceeded your rate limit. Waiting for 60 seconds before retrying..."
        )
        response_message = "โปรดทำรายการใหม่ในภายหลัง"
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        print("An unexpected error occurred. Please check the application logs.")
    
    while finish_reason == "length":

        max_tokens = max_tokens + 500
        
        print(f"max_tokens:{max_tokens}")

        try:

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0.2,
                top_p=0.2,
                max_tokens=max_tokens,
            )

            finish_reason = response["choices"][0]["finish_reason"] 
            response_message = response["choices"][0]["message"]["content"]

            print(finish_reason)
            print(response_message)

        except openai.error.AuthenticationError:
            logging.error("AuthenticationError: Invalid API key.")
            print(
                "There was a problem with your authentication. Please check your API key."
            )
        except openai.error.InvalidRequestError:
            logging.error("InvalidRequestError: Invalid API request.")
            print("You made an invalid request. Please check the provided parameters.")
        except openai.error.RateLimitError:
            logging.error("RateLimitError: API request limit exceeded.")
            print(
                "You've exceeded your rate limit. Waiting for 60 seconds before retrying..."
            )
            response_message = "โปรดทำรายการใหม่ในภายหลัง"
        except Exception as e:
            logging.error(f"Unexpected error: {str(e)}")
            print("An unexpected error occurred. Please check the application logs.")

        if max_tokens > 3000:
            break

    return response_message

def get_history_message(sender):
    print("get_history_message running")

    url = f"{fb_api_url}{page_id}/conversations/?user_id={sender}&access_token={fb_page_access_token}&fields=messages"

    response = requests.request("GET", url, headers={}, data={})

    chat_history = []
    
    chat_ids = response.json()["data"][0]["messages"]["data"]

    for chat in chat_ids[:message_count]:
        messages_id = chat["id"]

        if is_old_message(chat["created_time"]):
            continue

        get_message_response = get_message(messages_id)
        message = get_message_response["message"]
        from_id = get_message_response["from"]["id"]
        chat_history.append({"message":message, "from_id":from_id})

    return chat_history

def get_message(messages_id):
    url = f"{fb_api_url}{messages_id}?access_token={fb_page_access_token}&fields=from,message"
    response = requests.request("GET", url, headers={}, data={})
    return response.json()

def convert_to_chatgpt_message(chat_history, system_role_txt):

    messages = [{"role": "system", "content": system_role_txt}]

    for chat in chat_history[::-1]:

        role = "user"

        if chat["from_id"]==page_id:
            role = "assistant"

        content  = chat["message"]

        messages.append({"role":role, "content":content})
    
    last_message = messages[-1]["content"]
    last_message = "answer briefly in thai only:"+last_message
    messages[-1] = {"role":role, "content":last_message}

    return messages

def is_old_message(iso_string):
    # Remove the '+' from the timezone offset because fromisoformat() cannot parse it
    iso_string = iso_string.replace("+0000", "")
    # Convert to a datetime object
    dt_object = datetime.fromisoformat(iso_string)
    # Get current time
    now = datetime.utcnow()
    # Check if the difference is greater than old minute
    return (now - dt_object) > timedelta(days=old_day)

def is_processed(message_id):
    if message_id in processed_message_ids:
        return True
    processed_message_ids.add(message_id)
    return False

def get_system_role():
    with open('system_role.txt', 'r', encoding='utf-8') as file:
        return file.read().strip()