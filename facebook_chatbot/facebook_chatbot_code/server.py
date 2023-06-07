from flask import Flask, request
import requests
import hmac
import hashlib
import json

app = Flask(__name__)
app_secret = "your_app_secret"

def verify_webhook(req):
    print("verify_webhook running")
    calling_verify_token = req.args.get("hub.verify_token")
    print(f"calling_verify_token : {calling_verify_token}")
    fb_verify_token = "fb_verify_token_pree"
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
                    reply_message = f"reply for:{text}"
                    send_message(sender_id, reply_message)
            return "ok"
        else:
            return "invalid"

def send_message(recipient_id, reply_message):
    """Send a response to Facebook"""
    fb_page_access_token = "your_page_access_token"
    fb_api_url = "https://graph.facebook.com/v2.6/"

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
    print(response.json())
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