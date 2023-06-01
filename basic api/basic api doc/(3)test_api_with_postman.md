# Using Postman to Test Your Flask Application

**Postman** is a powerful tool used for testing API endpoints. In this document, we will cover how to install Postman and use it to test our Flask application.

## 1. **Install Postman:** 

- Visit the official [Postman downloads page](https://www.postman.com/downloads/).
- Download the version suitable for your operating system and install it.

## 2. **Using Postman to Test Flask Endpoints:** 

Once installed, you can open Postman and use it to send requests to your Flask application.

Here are the steps to test the endpoints:

### **Testing /get1 endpoint:**

- In Postman, select "GET" from the dropdown list.
- Enter the following URL, replacing `<your_ngrok_url>` with your actual ngrok URL, and `name` with your actual name:

```
http://<your_ngrok_url>/get1?name=test
```

- Click the "Send" button. You should see a response saying "your input name is test".

### **Testing /get2 endpoint:**

- In Postman, select "GET" from the dropdown list.
- Enter the following URL, replacing `<your_ngrok_url>` with your actual ngrok URL, and `name` with the name of the teacher ("pree" or "krin"):

```
http://<your_ngrok_url>/get2?name=pree
```

- Click the "Send" button. You should see a response saying "your teacher age is 27" if the teacher's name is "pree", or "your teacher age is 28" if the teacher's name is "krin".

### **Testing /post1 endpoint:**

- In Postman, select "POST" from the dropdown list.
- Enter the following URL, replacing `<your_ngrok_url>` with your actual ngrok URL:

```
http://<your_ngrok_url>/post1
```

- In the "Body" tab, select "raw" and "JSON" from the dropdown lists.
- Enter a JSON body with any data, for example:

```json
{
    "name": "test",
    "age": 30
}
```

- Click the "Send" button. You should see a response saying "ok your input data is" followed by the data you entered.

### **Testing /post2 endpoint:**

- In Postman, select "POST" from the dropdown list.
- Enter the following URL, replacing `<your_ngrok_url>` with your actual ngrok URL:

```
http://<your_ngrok_url>/post2
```

- In the "Body" tab, select "raw" and "JSON" from the dropdown lists.
- Enter a JSON body with the "search_name" field set to the name of the teacher you want to search for, for example:

```json
{
    "search_name": "krin"
}
```

- Click the "Send" button. You should see a response saying "your teacher age is 28" if the teacher's name is "krin", or "your teacher age is 27" if the teacher's name is "pree".

---