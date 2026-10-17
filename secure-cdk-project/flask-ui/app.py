from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

API_URL = os.environ.get("API_URL")
API_KEY = os.environ.get("API_KEY")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    content = file.read()

    headers = {
        "x-api-key": API_KEY
    }

    res = requests.post(API_URL, headers=headers, data=content)

    return res.text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)