from flask import Flask, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

from routes.describe import describe_bp
app.register_blueprint(describe_bp)


@app.route("/")
def home():
    return jsonify({"message": "AI Service Running"})


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


if __name__ == "__main__":
    app.run(debug=True)