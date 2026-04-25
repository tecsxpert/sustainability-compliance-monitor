from flask import Flask
from routes.describe import describe_bp
from routes.recommend import recommend_bp

app = Flask(__name__)

app.register_blueprint(describe_bp)
app.register_blueprint(recommend_bp)

@app.route("/health", methods=["GET"])
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)