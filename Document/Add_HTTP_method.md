# Enhancing your Flask application with GET and POST methods:

## 1. **Import necessary modules:** 

For the next steps, we need to import some additional modules to our Flask application. Update your `app.py` file to import the `request` and `json` modules as follows:

```python
from flask import Flask, request
import json
```

## 2. **Add a GET Method to Receive URL parameters:** 

This method will read data from the URL parameters. Add the following function to `app.py`:

```python
@app.route("/get1", methods=["GET"])
def read_get_data():
    name = request.args.get("name")
    return "your input name is " + name
```

## 3. **Add a GET Method with Search Logic:** 

This method will read data from the URL parameters and perform some search logic. Add the following function to `app.py`:

```python
@app.route("/get2", methods=["GET"])
def find_teacher_age_get():
    data = {
        "teacher":[
            {
                "name":"pree",
                "age":27
            },
            {
                "name":"krin",
                "age":28
            }
        ]
    }
    name = request.args.get("name")

    age = "not found"

    for teacher in data["teacher"]:
        if teacher["name"] == name:
            age = str(teacher["age"])

    return "your teacher age is " + age
```

## 4. **Add a POST Method to Receive JSON request body:** 

This method will read data from a POST request's JSON body. Add the following function to `app.py`:

```python
@app.route("/post1", methods=["POST"])
def read_post_data():
    payload = request.json
    return "ok your input data is" + json.dumps(payload)
```

## 5. **Add a POST Method with Search Logic:** 

This method will read data from a POST request's JSON body and perform some search logic. Add the following function to `app.py`:

```python
@app.route("/post2", methods=["POST"])
def find_teacher_age_post():
    data = {
        "teacher":[
            {
                "name":"pree",
                "age":27
            },
            {
                "name":"krin",
                "age":28
            }
        ]
    }

    payload = request.json
    name = payload["search_name"]
    age = "not found"
    for teacher in data["teacher"]:
        if teacher["name"] == name:
            age = str(teacher["age"])

    return "your teacher age is " + age
```

Now your application can handle both GET and POST requests and perform simple operations with the incoming data. Don't forget to restart your Flask server to apply these changes.