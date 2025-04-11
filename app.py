from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
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

if __name__ == "__main__":
    app.run(debug=True)