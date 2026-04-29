from flask import Blueprint, request, jsonify
from services.groq_client import generate_response
from datetime import datetime
import os
import json

describe_bp = Blueprint("describe", __name__)

@describe_bp.route("/describe", methods=["POST"])
def describe():
    try:
        data = request.get_json()

        # STEP 1: VALIDATION
        if not data or "input_text" not in data:
            return jsonify({"error": "input_text is required"}), 400

        input_text = data["input_text"].strip()

        if input_text == "":
            return jsonify({"error": "input_text cannot be empty"}), 400

        # STEP 2: LOAD PROMPT
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        prompt_path = os.path.join(BASE_DIR, "prompts", "describe_prompt.txt")

        with open(prompt_path, "r") as f:
            template = f.read()

        # STEP 3: INJECT INPUT
        final_prompt = template.replace("{input_text}", input_text)

        # STEP 4: CALL GROQ
        response = generate_response(final_prompt)

        # STEP 5: FALLBACK
        if response is None:
            return jsonify({
                "input": input_text,
                "description": "AI service unavailable. Try again later.",
                "generated_at": datetime.utcnow().isoformat(),
                "is_fallback": True
            }), 200

        # STEP 6: PARSE JSON (important)
        try:
            parsed = json.loads(response)
        except:
            parsed = response  # fallback if not valid JSON

        # STEP 7: SUCCESS RESPONSE
        return jsonify({
            "input": input_text,
            "description": parsed,
            "generated_at": datetime.utcnow().isoformat(),
            "is_fallback": False
        }), 200

    except Exception as e:
        return jsonify({
            "error": "Internal Server Error",
            "details": str(e)
        }), 500