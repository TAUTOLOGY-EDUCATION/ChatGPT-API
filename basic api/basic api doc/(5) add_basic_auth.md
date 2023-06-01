# Adding Basic Authentication to Your Flask Application

In this guide, you will add basic password-based authentication to your Flask API. This will allow you to secure your API endpoints by ensuring that only authenticated users with the correct password can access them.

## 1. **Add a GET Method with Password Authentication:**

To do this, we will add a password check to the existing GET endpoint. The password will be sent in the headers of the HTTP request. Add the following function to `app.py`:

```python
password = "12345678"  # Global password variable

@app.route("/get3", methods=["GET"])
def get_with_auth():
    req_password = request.headers.get("password")

    if req_password == password:
        name = request.args.get("name")
        return "your input name is " + name
    else:
        return "invalid password", 401  # Return HTTP 401 Unauthorized status code
```

## 2. **Add a POST Method with Password Authentication:**

Similar to the GET method, we will also add a password check for the POST endpoint. Add the following function to `app.py`:

```python
@app.route("/post3", methods=["POST"])
def post_with_auth():
    req_password = request.headers.get("password")

    if req_password == password:
        payload = request.json
        return "your input data is " + json.dumps(payload)
    else:
        return "invalid password", 401  # Return HTTP 401 Unauthorized status code
```

Note that we're using `request.headers.get("password")` to get the password from the request headers. If the password matches the global password variable, the endpoint will process the request as usual. If not, it will return a response of "Invalid password" with a 401 Unauthorized HTTP status code.

Now your Flask application is ready to handle GET and POST requests with simple password-based authentication. Remember to replace "12345678" with your actual password and do not expose this password in your production environment.