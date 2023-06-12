from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/part1')
def hello():
    return 'Hello'

@app.route("/get1", methods=["GET"])
def read_get_data():
    name = request.args.get("name")
    return "your input name is " + name

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

@app.route("/post1", methods=["POST"])
def read_post_data():
    payload = request.json
    return "your input data is " + json.dumps(payload)

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


password = "12345678"  # Global password variable

@app.route("/get3", methods=["GET"])
def get_with_auth():
    req_password = request.headers.get("password")

    if req_password == password:
        name = request.args.get("name")
        return "your input name is " + name
    else:
        return "invalid password", 401  # Return HTTP 401 Unauthorized status code

@app.route("/post3", methods=["POST"])
def post_with_auth():
    req_password = request.headers.get("password")

    if req_password == password:
        payload = request.json
        return "your input data is " + json.dumps(payload)
    else:
        return "invalid password", 401  # Return HTTP 401 Unauthorized status code
