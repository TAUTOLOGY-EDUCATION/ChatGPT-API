# Create your first Facebook Chatbot

This guide will walk you through the steps of creating a simple chatbot on Facebook using the Facebook Messenger Platform.

## 1. **Create a Facebook Page**

You'll need a Facebook page to attach the chatbot to. If you already have one, you can skip this step. If not, you can create one by following the steps:

- Go to [Facebook Pages](https://www.facebook.com/pages/create/)
- Click to choose a Page type
- Fill out the required information
- Click Create Page

## 2. **Create a Developer Account**

To create a chatbot, you need a developer account on Facebook.

- Visit [Facebook Developers](https://developers.facebook.com/)
- Click "Get Started" in the top right corner
- Follow the prompts to register as a developer

## 3. **Create an App**

- From the [Developer Dashboard](https://developers.facebook.com/apps/), click "Create App" 
- Select "Business" as the purpose of your app and click "Continue"
- Fill in the details about your app and then click "Create App"

## 4. **Generate a Page Messenger Token**

- Go to your App Dashboard
- Click "Set Up" in the Messenger section
- Select the page you want to generate a token for in the dropdown
- Click "Generate Token"
- Copy the generated token and keep it safe, as it will not be shown again

## 5. **Verify Webhook**

To communicate with the Facebook server, you'll need to set up a webhook. This involves creating a Flask endpoint to accept these webhook events:

```python
@app.route("/webhook", methods=["GET","POST"])
def listen():
    print(f"calling webhook method : {request.method}")
    """This is the main function flask uses to 
    listen at the `/webhook` endpoint"""
    if request.method == "GET":
        return verify_webhook(request)
    if request.method == "POST":
        return send_message(sender, response)
```

Additionally, here's a sample `verify_webhook` function:

```python
def verify_webhook(req):
    print("verify_webhook running")
    calling_verify_token= req.args.get("hub.verify_token")
    print(f"calling_verify_token : {calling_verify_token}")
    fb_verify_token = "<Your Verification Token>"
    if calling_verify_token == fb_verify_token:
        challenge = req.args.get("hub.challenge")
        return challenge
    else:
        return "incorrect"
```

Please replace `"<Your Verification Token>"` with your actual Facebook verification token.

- Use ngrok or a similar service to create a secure tunnel to your webhook.
- In your app settings on Facebook, set the Callback URL to your ngrok URL + /webhook.
- The verify token should be the same one you put in your `verify_webhook` function.
- After you set the Callback URL and Verify Token, click "Verify and Save".

## 6. **Edit Page Subscriptions**

You'll need to set up your page subscription to receive messages and postbacks:

- Go back to the Messenger settings in your app dashboard
- Under "Webhooks", click "Edit Callback URL"
- Enter your Callback URL and Verify Token again
- In the "Subscription Fields" section, select "messages" and "messaging_postbacks"
- Click "Save"

Now, whenever a user sends a message or clicks a postback button in your chatbot, Facebook will send an HTTP POST request to your webhook.

Congratulations! You have now successfully created a Facebook Chatbot. The next steps would be to enhance the bot's functionality by creating responses to user inputs.