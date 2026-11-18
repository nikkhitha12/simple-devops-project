from flask import Flask

app = Flask(__name__)


@app.route("/message")
def message():
    return {
        "message": "Hello from Container 2!"
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)