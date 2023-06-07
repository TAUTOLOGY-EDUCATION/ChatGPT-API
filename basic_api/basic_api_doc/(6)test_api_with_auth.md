# Testing Flask Endpoints With Authentication

In this guide, we'll walk you through testing the GET and POST methods that require password-based authentication in your Flask API using both Postman and Jupyter notebook.

## 1. **Postman Testing**

### **Testing the GET Method:**

- In Postman, select "GET" from the dropdown list.
- Enter the following URL, replacing `<your_ngrok_url>` with your actual ngrok URL, and `name` with your actual name:

```
http://<your_ngrok_url>/get3?name=test
```
- Click on the Headers tab and add a new key `password` and set its value to `12345678`.
- Click the "Send" button.

If your password is correct, you should see a response like `your input name is test`.

### **Testing the POST Method:**

- In Postman, select "POST" from the dropdown list.
- Enter the following URL, replacing `<your_ngrok_url>` with your actual ngrok URL:

```
http://<your_ngrok_url>/post3
```
- Click on the Headers tab and add a new key `password` and set its value to `12345678`.
- In the "Body" tab, select "raw" and "JSON" from the dropdown lists.
- Input your JSON payload. For example: `{"search_name": "pree"}`
- Click the "Send" button.

If your password is correct, you should see a response like `ok your input data is ` followed by the JSON payload you sent.

## 2. **Jupyter Notebook Testing**

You can use the `requests` library in Python to make HTTP requests. Make sure it is installed by running `!pip install requests` in a Jupyter cell.

### **Testing the GET Method:**

```python
url = "http://<your_ngrok_url>/get3?name=pree"

payload = {}
headers = {"password":"12345678"}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

### **Testing the POST Method:**

```python
url = "http://<your_ngrok_url>/post3"

payload = json.dumps({
  "search_name": "pree"
})
headers = {
  'password': '12345678',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

You should see the response from the server printed in the output of the cell.

Remember to replace "12345678" with the password you have set, and `<your_ngrok_url>` with the URL of your application.