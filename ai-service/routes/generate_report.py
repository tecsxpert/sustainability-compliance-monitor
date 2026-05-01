from flask import Blueprint, request, jsonify
import time
from services.groq_client import call_groq
from services.fallback import fallback_report
from config import REPORT_PROMPT

report_bp = Blueprint('report', __name__)

@report_bp.route("/generate-report", methods=["POST"])
def generate_report():
    start_time = time.time()

    data = request.json

    if not data or "text" not in data:
        return jsonify({"error": "Invalid input"}), 400

    messages = [
        {"role": "system", "content": REPORT_PROMPT},
        {"role": "user", "content": data["text"]}
    ]

    result = call_groq(messages, fallback_report)

    response_time = round(time.time() - start_time, 2)

    return jsonify({
        "report": result["data"],
        "is_fallback": result["is_fallback"],
        "response_time": response_time
    })