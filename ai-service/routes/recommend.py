from flask import Blueprint, request, jsonify
from services.recommend_service import generate_recommendations
from datetime import datetime

recommend_bp = Blueprint("recommend", __name__)

@recommend_bp.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()

    # Input validation
    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' field"}), 400

    input_text = data["text"]

    if not input_text.strip():
        return jsonify({"error": "Input cannot be empty"}), 400

    # Call service
    result = generate_recommendations(input_text)

    return jsonify({
        "recommendations": result,
        "generated_at": datetime.utcnow().isoformat()
    }), 200