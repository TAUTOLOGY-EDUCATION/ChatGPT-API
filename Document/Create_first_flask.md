# Create your first Flask application steps

## 1. **Setup your development environment:** 

First, you need to have Python installed. You can download Python from the official website [Python](https://www.python.org/downloads/). Flask works with Python 3.5 and later versions.

## 2. **Create a new directory:** 

Create a new directory for your Flask project and navigate to it using your terminal or command prompt.

## 3. **Create a virtual environment:** 

Create virtual environment by running the command. Use the following commands to create a new virtual environment:

```bash
python3 -m venv environment_name
```
Then, to activate the virtual environment, you'll use:

- On Windows:

```bash
environment_name\Scripts\activate.bat
```

- On Unix or MacOS:

```bash
source environment_name/bin/activate
```

## 4. **Install Flask:** 

After activating your virtual environment, you can install Flask using pip:

```bash
pip install flask
```

## 5. **Create your Flask application:** 

Now you can start creating your Flask application. In your project directory, create a new Python file (for example, `app.py`), and add the following code:

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
```

This is a simple Flask application that defines a single route ("/") which returns the string "Hello, World!" when accessed.

## 6. **Run your Flask application:** 

To run your application, use the `flask run` command. But before that, you need to set the `FLASK_APP` environment variable to point to your application. Here is how you can do it:

- On Windows:

```bash
$env:FLASK_APP = 'app.py'
flask run --port 5000
```

- On Unix or MacOS:

```bash
export FLASK_APP=app.py
flask run --port 5000
```

Now you can open your web browser and navigate to `http://localhost:5000`. You should see "Hello, World!" displayed.

## 7. **Create a Public Endpoint with ngrok:**

   - **Download and install ngrok:** Visit the [ngrok download page](https://ngrok.com/download) and follow the instructions for your operating system.
   
   - **Connect your ngrok account:** You will need an ngrok account to expose your local server to the internet. After creating your account, navigate to the [ngrok dashboard](https://dashboard.ngrok.com/get-started/your-authtoken) to get your authtoken.
   
   - **Add your ngrok authtoken:** In your terminal or command prompt, enter the following command to add your ngrok authtoken:
   
   ```bash
   ngrok config add-authtoken <your_ngrok_authtoken>
   ```
   
   - **Create a tunnel to your Flask application:** With ngrok installed and your Flask app running, you can create a public URL with the following command:
   
   ```bash
   ngrok.exe http 5000
   ```
   
## 8. **Access your Flask application over the internet:** 

After running ngrok, you'll see an output like this:

```bash
Forwarding    http://<some_url> -> localhost:5000  
```

You can copy this ngrok.io URL and paste it into any browser to access your Flask application.

---