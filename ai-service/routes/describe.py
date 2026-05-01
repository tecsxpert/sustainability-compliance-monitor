from flask import Blueprint, request, jsonify
import time
from services.groq_client import call_groq
from services.fallback import fallback_describe
from config import DESCRIBE_PROMPT

describe_bp = Blueprint('describe', __name__)

@describe_bp.route("/describe", methods=["POST"])
def describe():
    start_time = time.time()

    data = request.json

    if not data or "text" not in data:
        return jsonify({"error": "Invalid input"}), 400

    messages = [
        {"role": "system", "content": DESCRIBE_PROMPT},
        {"role": "user", "content": data["text"]}
    ]

    #  CALL YOUR FUNCTION HERE
    result = call_groq(messages, fallback_describe)

    return jsonify({
        "result": result["data"],
        "is_fallback": result["is_fallback"],
        "response_time": round(time.time() - start_time, 2)
    })