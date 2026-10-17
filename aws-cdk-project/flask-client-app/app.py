from flask import Flask, render_template, request
import requests
import base64

app = Flask(__name__)

API_URL = "https://<your-api-id>.execute-api.ap-south-1.amazonaws.com/prod/upload"
API_KEY = "<your-api-key>"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]

    content = base64.b64encode(file.read()).decode()

    payload = {
        "filename": file.filename,
        "content": content
    }

    headers = {
        "x-api-key": API_KEY
    }

    r = requests.post(API_URL, json=payload, headers=headers)

    return f"Response: {r.text}"


if __name__ == "__main__":
    app.run(debug=True)