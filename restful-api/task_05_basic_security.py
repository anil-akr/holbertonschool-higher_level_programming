#!/usr/bin/python3
"""
task_05_basic_security.py

Flask API demonstrating:
- Basic HTTP Authentication
- JWT Authentication
- Role-based access control
- Proper authentication error handling (401 responses)
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Strong secret key (required for JWT)
app.config["JWT_SECRET_KEY"] = "super-secret-key"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# In-memory users store
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# =========================
# BASIC AUTHENTICATION
# =========================

@auth.verify_password
def verify_password(username, password):
    """
    Verify username and password for Basic Authentication.
    """
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None


@auth.error_handler
def basic_auth_error(status):
    """
    Ensure Basic Auth errors return 401.
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """
    Route protected by Basic Authentication.
    """
    return "Basic Auth: Access Granted"


# =========================
# JWT ERROR HANDLERS
# =========================

@jwt.unauthorized_loader
def handle_missing_token(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_fresh_token_required(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401


# =========================
# JWT AUTHENTICATION
# =========================

@app.route("/login", methods=["POST"])
def login():
    """
    Authenticate user and return JWT token.
    """
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = users.get(username)

    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Embed role in JWT identity
    access_token = create_access_token(
        identity={"username": username, "role": user["role"]}
    )

    return jsonify({"access_token": access_token})


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """
    Route protected by JWT.
    """
    return "JWT Auth: Access Granted"


# =========================
# ROLE-BASED ACCESS CONTROL
# =========================

@app.route("/admin-only")
@jwt_required()
def admin_only():
    """
    Route accessible only to admin users.
    """
    current_user = get_jwt_identity()

    if current_user.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run()
