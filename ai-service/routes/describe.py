from flask import Blueprint, request, jsonify
from services.groq_client import generate_response
from datetime import datetime
import json
import os

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

        # STEP 2: LOAD PROMPT (ROBUST PATH)
        try:
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            prompt_path = os.path.join(BASE_DIR, "..", "prompts", "describe_prompt.txt")

            with open(prompt_path, "r") as f:
                prompt_template = f.read()

        except Exception as e:
            print("Prompt Load Error:", str(e))
            return jsonify({"error": "Prompt file not found"}), 500

        # STEP 3: INJECT INPUT INTO PROMPT
        final_prompt = prompt_template.replace("{input_text}", input_text)

        # STEP 4: CALL GROQ
        response = generate_response(final_prompt)
        print("Groq response:", response)

        # STEP 5: FALLBACK HANDLING
        if response is None:
            return jsonify({
                "input": input_text,
                "description": "AI service unavailable. Try again later.",
                "generated_at": datetime.utcnow().isoformat(),
                "is_fallback": True
            }), 200

        # STEP 6: PARSE JSON RESPONSE
        try:
            parsed_response = json.loads(response)
        except Exception:
            parsed_response = {"raw_output": response}

        # STEP 7: SUCCESS RESPONSE
        return jsonify({
            "input": input_text,
            "description": parsed_response,
            "generated_at": datetime.utcnow().isoformat(),
            "is_fallback": False
        }), 200

    except Exception as e:
        print("Internal Error:", str(e))
        return jsonify({
            "error": "Internal Server Error",
            "details": str(e)
        }), 500