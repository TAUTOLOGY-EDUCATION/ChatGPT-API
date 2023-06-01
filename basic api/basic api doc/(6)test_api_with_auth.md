# Testing Flask Endpoints With Authentication

In this guide, we'll walk you through testing the GET and POST methods that require password-based authentication in your Flask API using both Postman and Jupyter notebook.

## 1. **Postman Testing**

### **Testing the GET Method:**

- Launch Postman and create a new GET request.
- In the request URL field, type in your API's URL followed by `/get3`. For example, if your API is running on ngrok, the URL will be `http://<your_ngrok_url>/get3`.
- In the params tab, add your key-value pair. For instance, if you want to send `name`, put `name` in the key and its value in the value field.
- Click on the Headers tab and add a new key `password` and set its value to `12345678`.
- Click the Send button to make the request.

If your password is correct, you should see a response like `your input name is ` followed by the name you input.

### **Testing the POST Method:**

- Create a new POST request.
- In the request URL field, type in your API's URL followed by `/post3`.
- Click on the Headers tab and add a new key `password` and set its value to `12345678`.
- Click on the Body tab, select `raw` and `JSON` format.
- Input your JSON payload. For example: `{"search_name": "pree"}`
- Click the Send button to make the request.

If your password is correct, you should see a response like `ok your input data is ` followed by the JSON payload you sent.

## 2. **Jupyter Notebook Testing**

You can use the `requests` library in Python to make HTTP requests. Make sure it is installed by running `!pip install requests` in a Jupyter cell.

### **Testing the GET Method:**

```python
import requests

url = "http://<your_ngrok_url>/get3"
headers = {"password": "12345678"}
params = {"name": "pree"}

response = requests.get(url, headers=headers, params=params)
print(response.text)
```

### **Testing the POST Method:**

```python
import requests
import json

url = "http://<your_ngrok_url>/post3"
headers = {"password": "12345678", "Content-Type": "application/json"}
data = {"search_name": "pree"}

response = requests.post(url, headers=headers, data=json.dumps(data))
print(response.text)
```

You should see the response from the server printed in the output of the cell.

Remember to replace "12345678" with the password you have set, and `<your_ngrok_url>` with the URL of your application.