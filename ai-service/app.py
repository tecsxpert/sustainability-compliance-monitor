from flask import Flask
from routes.describe import describe_bp
from routes.recommend import recommend_bp

# ✅ FIRST create app
app = Flask(__name__)

# ✅ THEN register blueprints
app.register_blueprint(describe_bp)
app.register_blueprint(recommend_bp)

# ✅ Run server
if __name__ == "__main__":
    app.run(debug=True)