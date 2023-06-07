from flask import Flask, request
import requests

app = Flask(__name__)

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
    print(f"Calling webhook method : {request.method}")
    """This is the main function Flask uses to 
    listen at the `/webhook` endpoint"""
    if request.method == "GET":
        return verify_webhook(request)
    if request.method == "POST":
        payload = request.json
        event = payload["entry"][0]["messaging"]
        for x in event:
            text = x["message"]["text"]
            sender_id = x["sender"]["id"]
            reply_message = f"reply for:{text}"
            send_message(sender_id, reply_message)
        return "ok"

def send_message(recipient_id, reply_message):
    """Send a response to Facebook"""
    fb_page_access_token = "EAACwoj4hoVcBAC7OCDDa78p4ZC2tGztuUeNpCjURzQjdyTtKe6VIjSwfZB89MUAYcOXZA3M6sQo1c3lFAJ5gDVcLkL5jOD6dosnSFcJB8MUxuyihVNMXeLxWFTcUy5HGxBD3XGSlqON31ZA9lmZAibxhgsbjYStQpwTulCNjb96HhysZCRThjo"
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
    return response.json()