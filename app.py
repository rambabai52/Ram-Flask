from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
   return "Hello, this is my updated Flask app!" 


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, this is my updated Flask app!"

@app.route("/about")
def about():
    return "This is the About page of my Flask app."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
