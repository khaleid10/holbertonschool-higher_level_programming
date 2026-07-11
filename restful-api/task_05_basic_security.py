#!/usr/bin/python3
"""Basic API Security with Flask."""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
    get_jwt,
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret-key"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# In-memory users
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


# --------------------------
# Basic Authentication
# --------------------------

@auth.verify_password
def verify_password(username, password):
    """Verify username and password."""
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None


@auth.error_handler
def auth_error(status):
    """Return 401 for authentication errors."""
    return jsonify({"error": "Unauthorized"}), 401


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """Basic Auth protected endpoint."""
    return "Basic Auth: Access Granted", 200


# --------------------------
# JWT Authentication
# --------------------------

@app.route("/login", methods=["POST"])
def login():
    """Authenticate user and return JWT."""
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid credentials"}), 401

    username = data.get("username")
    password = data.get("password")

    user = users.get(username)

    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(
        identity=username,
        additional_claims={"role": user["role"]}
    )

    return jsonify(access_token=token), 200


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """JWT protected endpoint."""
    get_jwt_identity()
    return "JWT Auth: Access Granted", 200


# --------------------------
# Role-based Authorization
# --------------------------

@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """Admin only endpoint."""
    claims = get_jwt()

    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted", 200


# --------------------------
# JWT Error Handlers
# --------------------------

@jwt.unauthorized_loader
def unauthorized_callback(error):
    """Missing token."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def invalid_token_callback(error):
    """Invalid token."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    """Expired token."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def revoked_token_callback(jwt_header, jwt_payload):
    """Revoked token."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def fresh_token_callback(jwt_header, jwt_payload):
    """Fresh token required."""
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run(debug=True)
