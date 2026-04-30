from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from werkzeug.exceptions import HTTPException
from werkzeug.serving import WSGIRequestHandler
import time

app = Flask(__name__)

# ---------------------------
# Disable debug leaks
# ---------------------------
app.config["DEBUG"] = False
app.config["PROPAGATE_EXCEPTIONS"] = False

# ---------------------------
# Remove Server Header (FINAL FIX)
# ---------------------------


class NoServerHeaderHandler(WSGIRequestHandler):
    def version_string(self):
        return ""  # remove version

    def send_response(self, code, message=None):
        super().send_response(code, message)

    def end_headers(self):
        # remove Server header completely
        self._headers_buffer = [
            h for h in self._headers_buffer
            if not h.lower().startswith(b"server:")
        ]
        super().end_headers()
# ---------------------------
# Rate Limiting
# ---------------------------
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["30 per minute"]
)

# ---------------------------
# Security Headers
# ---------------------------
@app.after_request
def add_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    response.headers["Referrer-Policy"] = "no-referrer"

    # Remove server header if still present
    if "Server" in response.headers:
        del response.headers["Server"]

    return response


# ---------------------------
# Enforce JSON requests
# ---------------------------
@app.before_request
def enforce_json():
    if request.method == "POST" and not request.is_json:
        return jsonify({"error": "Only JSON requests allowed"}), 400


# ---------------------------
# Input validation
# ---------------------------
def validate_input(text):
    return text and len(text.strip()) > 0 and len(text) < 1000


# ---------------------------
# Root endpoint
# ---------------------------
@app.route("/")
def home():
    return jsonify({
        "message": "AI Service Running",
        "endpoints": [
            "/health",
            "/describe",
            "/recommend",
            "/generate-report"
        ]
    }), 200


# ---------------------------
# Health endpoint
# ---------------------------
@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


# ---------------------------
# Dummy AI logic
# ---------------------------
def generate_description(text):
    return {
        "description": f"AI description for: {text}",
        "generated_at": time.time()
    }


def generate_recommendations(text):
    return [
        {"action_type": "Reduce Waste", "description": "Improve recycling", "priority": "High"},
        {"action_type": "Energy Efficiency", "description": "Use LED lights", "priority": "Medium"},
        {"action_type": "Water Saving", "description": "Install low-flow taps", "priority": "Low"}
    ]


def generate_report(text):
    return {
        "title": "Sustainability Report",
        "summary": "Summary of compliance",
        "overview": text,
        "recommendations": generate_recommendations(text)
    }


# ---------------------------
# API: Describe
# ---------------------------
@app.route("/describe", methods=["POST"])
def describe():
    try:
        text = request.json.get("text", "")
        if not validate_input(text):
            return jsonify({"error": "Invalid input"}), 400
        return jsonify(generate_description(text))
    except:
        return jsonify({"error": "Internal server error"}), 500


# ---------------------------
# API: Recommend
# ---------------------------
@app.route("/recommend", methods=["POST"])
def recommend():
    try:
        text = request.json.get("text", "")
        if not validate_input(text):
            return jsonify({"error": "Invalid input"}), 400
        return jsonify(generate_recommendations(text))
    except:
        return jsonify({"error": "Internal server error"}), 500


# ---------------------------
# API: Generate Report
# ---------------------------
@app.route("/generate-report", methods=["POST"])
def generate_report_api():
    try:
        text = request.json.get("text", "")
        if not validate_input(text):
            return jsonify({"error": "Invalid input"}), 400
        return jsonify(generate_report(text))
    except:
        return jsonify({"error": "Internal server error"}), 500


# ---------------------------
# Handle HTTP errors (404 etc.)
# ---------------------------
@app.errorhandler(HTTPException)
def handle_http_error(e):
    return jsonify({"error": "Request failed"}), e.code


# ---------------------------
# Catch ALL errors
# ---------------------------
@app.errorhandler(Exception)
def handle_all_errors(e):
    return jsonify({"error": "Internal server error"}), 500


# ---------------------------
# Run App (IMPORTANT)
# ---------------------------
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False,
        request_handler=NoServerHeaderHandler
    )