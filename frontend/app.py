from flask import Flask
import requests

app = Flask(__name__)


@app.route("/")
def home():
    response = requests.get("http://backend:8000/message")

    return f"""
    <h1>Simple DevOps Application</h1>
    <p>{response.json()["message"]}</p>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)