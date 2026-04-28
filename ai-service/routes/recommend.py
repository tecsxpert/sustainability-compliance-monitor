from flask import Blueprint, request, jsonify
from datetime import datetime
from services.recommend_service import generate_recommendations

recommend_bp = Blueprint("recommend", __name__)


@recommend_bp.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()

    # Validation
    if not data or "text" not in data:
        return jsonify({"error": "text is required"}), 400

    text = data["text"].strip()

    if text == "":
        return jsonify({"error": "text cannot be empty"}), 400

    # Call service
    recommendations = generate_recommendations(text)

    return jsonify({
        "recommendations": recommendations,
        "generated_at": datetime.utcnow().isoformat()
    }), 200