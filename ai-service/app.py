from flask import Flask
from routes.describe import describe_bp
from routes.recommend import recommend_bp
from routes.generate_report import report_bp

app = Flask(__name__)

# Register routes
app.register_blueprint(describe_bp)
app.register_blueprint(recommend_bp)
app.register_blueprint(report_bp)

@app.route("/health", methods=["GET"])
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(port=5000, debug=True)