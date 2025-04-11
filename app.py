from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(name)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    prompt = f"Responda de forma simples, objetiva e sempre em português, seja sempre muito educado, sem exageros: {data['prompt']}"

    response = requests.post(
        "http://localhost:11434/api/generate",
        headers={"Content-Type": "application/json"},
        json={
            "model": "llava:7b-v1.6",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()
    return jsonify({"response": result["response"]})

<<<<<<< HEAD
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
=======
if name == "main":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
>>>>>>> 33959fe45405567785d4bd391a87a56cb2dbfa54
