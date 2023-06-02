# Testing Your Flask Application Using Python and Jupyter Notebook

Before testing the Flask application, you'll need to have Jupyter Notebook and Python's `requests` module installed. If you don't have them installed, you can install using the instructions below:

## 1. **Installing Jupyter Notebook**: 

You can install Jupyter Notebook using pip, the Python package installer. Open your terminal and type the following command:

```bash
pip install jupyter
```

## 2. **Installing requests module**: 

Python's `requests` module is a simple HTTP library for sending HTTP requests. It abstracts the complexities of making requests behind a beautiful, simple API so that you can focus on interacting with services and consuming data in your application. To install the requests module, open your terminal and type the following command:

```bash
pip install requests
```

## 3. **Start Jupyter Notebook**: 

You can start Jupyter Notebook by typing `jupyter notebook` in your terminal. This should open a new tab in your default web browser that shows the Notebook Dashboard.

```bash
jupyter notebook
```

## 4. **Testing with Jupyter**: 

With Jupyter Notebook and the `requests` module now installed, you are ready to start testing your Flask application:

First, import the `requests` module:

```python
import requests
import json
```

### **Testing /get1 endpoint:**

```python
url = "http://<your_ngrok_url>/get1?name=test"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

The response should be: "your input name is test".

### **Testing /get2 endpoint:**

```python
url = "http://<your_ngrok_url>/get2?name=pree"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

The response should be: "your teacher age is 27" if the teacher's name is "pree", or "your teacher age is 28" if the teacher's name is "krin".

### **Testing /post1 endpoint:**

```python
url = "http://<your_ngrok_url>/post1"

payload = json.dumps({"name": "test"})
headers = {"Content-Type": "application/json"}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

The response should be: "ok your input data is {'name': 'test', 'age': 30}".

### **Testing /post2 endpoint:**

```python
url = "http://<your_ngrok_url>/post2"

payload = json.dumps({"search_name": "krin"})
headers = {"Content-Type": "application/json"}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

The response should be: "your teacher age is 28" if the teacher's name is "krin", or "your teacher age is 27" if the teacher's name is "pree".

Remember to replace `<your_ngrok_url>` with the actual ngrok URL.

---