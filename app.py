from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)
from dotenv import load_dotenv
import os

load_dotenv()

HF_API_TOKEN = os.getenv("HF_API_TOKEN")
API_URL = "https://router.huggingface.co/hf-inference/models/facebook/bart-large-cnn"

def summarize_text(text, style):
    headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}

    if style == "brief":
        params = {"max_length": 60, "min_length": 20}
    elif style == "detailed":
        params = {"max_length": 200, "min_length": 80}
    elif style == "bullet":
        text = "Summarize into bullet points:\n" + text
        params = {"max_length": 150, "min_length": 50}
    else:
        params = {"max_length": 140, "min_length": 40}

    payload = {
        "inputs": text,
        "parameters": params
    }

    try:
        res = requests.post(API_URL, headers=headers, json=payload)
        data = res.json()

        if isinstance(data, dict) and "result" in data:
            r = data["result"]
            if isinstance(r, list) and len(r) > 0:
                if "summary_text" in r[0]:
                    return r[0]["summary_text"]
                if "generated_text" in r[0]:
                    return r[0]["generated_text"]

        if "summary_text" in data:
            return data["summary_text"]

        if isinstance(data, list) and "summary_text" in data[0]:
            return data[0]["summary_text"]

        return "Unexpected response format from HuggingFace."

    except Exception as e:
        return f"Error: {str(e)}"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/summarize", methods=["POST"])
def summarize():
    text = request.form.get("text", "")
    style = request.form.get("style", "brief")

    if not text.strip():
        return jsonify({"summary": "Error: Empty input!"})

    summary = summarize_text(text, style)
    return jsonify({"summary": summary})


if __name__ == "__main__":
    app.run(debug=True)

