from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

metrics = PrometheusMetrics(app)

@app.route("/")
def home():
    return jsonify({
        "service": "user-service",
        "version": "v1",
        "message": "User service is running"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "user-service"
    })

@app.route("/users")
def users():
    return jsonify({
        "users": [
            {"id": 1, "name": "Arya"},
            {"id": 2, "name": "DevOps User"}
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)