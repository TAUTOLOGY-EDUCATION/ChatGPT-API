# Add Facebook Request Validation and Authentication to Your Chatbot

In the previous guide, we discussed how to create a basic Facebook Messenger chatbot. This tutorial will focus on improving the chatbot's security by adding Facebook request validation and authentication.

In this guide, we are going to introduce two new methods, `validate_request(request)` and `is_user_message(x)`, into the Flask server code.

## 1. **Validate the Incoming Requests**

It is important to validate the requests coming from Facebook to ensure that your server is communicating only with Facebook and not any other third-party.

```python
import hmac
import hashlib
import json

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
```

This function first tries to obtain the `X-Hub-Signature-256` from the request headers. This is a SHA-256 signature of the request body, created using your app secret. The function then calculates the expected hash of the incoming request payload and compares it with the signature hash. If both match, the request is authenticated.

The `app_secret` is a string that you receive when you create your Facebook app.

## 2. **Check if the Message is from the User**

Facebook sends multiple types of messages, and not all of them are text messages from the user. It is essential to handle only the messages from the user.

```python
def is_user_message(message):
    """Check if the message is a message from the user"""
    return (message.get("message") and
            message["message"].get("text") and
            not message["message"].get("is_echo"))
```

This function checks if the message has the `message` and `text` fields and does not contain the `is_echo` field. The `is_echo` field is set to `True` for echo messages, delivery reports, or other types of messages that are not actual user messages.

## 3. **Integrate These Functions into the Main App**

Next, we will integrate these new functions into the main Flask server code. 

The new version of the `listen()` function is:

```python
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
```

Now, your Flask app is ready to handle and respond to user messages while validating every incoming request for security.



Remember to replace `<Your Verification Token>` and `<Your Page Access Token>` in the above code with your actual Facebook verification token and Facebook page access token, respectively. Also, you will need to provide the app secret as `app_secret` variable in your code.
