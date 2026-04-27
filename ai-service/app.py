from flask import Flask, jsonify
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create Flask app
app = Flask(__name__)

# Health check route
@app.route('/')
def home():
    return jsonify({
        "status": "success",
        "message": "AI Service is running",
        "port": 5000
    })

# Optional health endpoint (useful later)
@app.route('/health')
def health():
    return jsonify({
        "status": "healthy"
    })

# Run server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)