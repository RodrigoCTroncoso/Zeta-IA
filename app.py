import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    prompt = f"Responda de forma simples, objetiva e sempre em português, seja sempre muito educado, sem exageros: {data['prompt']}"
    
    response = requests.post(
        "https://d497-201-49-204-92.ngrok-free.app",
        headers={"Content-Type": "application/json"},
        json={
            "model": "llava:7b-v1.6",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()
    return jsonify({"response": result["response"]})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
