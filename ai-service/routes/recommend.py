from flask import Blueprint, request, jsonify
import time
from services.groq_client import call_groq
from services.fallback import fallback_recommend
from config import RECOMMEND_PROMPT

recommend_bp = Blueprint('recommend', __name__)

@recommend_bp.route("/recommend", methods=["POST"])
def recommend():
    start_time = time.time()

    data = request.json

    if not data or "text" not in data:
        return jsonify({"error": "Invalid input"}), 400

    messages = [
        {"role": "system", "content": RECOMMEND_PROMPT},
        {"role": "user", "content": data["text"]}
    ]

    result = call_groq(messages, fallback_recommend)

    response_time = round(time.time() - start_time, 2)

    return jsonify({
        "recommendations": result["data"],
        "is_fallback": result["is_fallback"],
        "response_time": response_time
    })