#!/usr/bin/python3
"""
task_04_flask.py

Simple REST API built with Flask.

This application demonstrates:
- Basic route handling
- Returning JSON responses
- Dynamic routes
- Handling POST requests
- Basic error handling
- In-memory data storage
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users
users = {}


@app.route("/")
def home():
    """
    Root endpoint.

    Returns:
        str: Welcome message.
    """
    return "Welcome to the Flask API!"


@app.route("/status")
def status():
    """
    Status endpoint.

    Returns:
        str: API status confirmation.
    """
    return "OK"


@app.route("/data")
def get_data():
    """
    Retrieve all usernames stored in memory.

    Returns:
        Response: JSON list of usernames.
    """
    return jsonify(list(users.keys()))


@app.route("/users/<username>")
def get_user(username):
    """
    Retrieve a specific user by username.

    Args:
        username (str): The username to search for.

    Returns:
        Response:
            - JSON user object if found (200)
            - JSON error message if not found (404)
    """
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Add a new user to the API.

    Expects JSON body with:
        - username (str)
        - name (str)
        - age (int)
        - city (str)

    Returns:
        Response:
            - 201 with confirmation and user data if successful
            - 400 if JSON is invalid
            - 400 if username is missing
            - 409 if username already exists
    """
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()

    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Store full user object
    users[username] = data

    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == "__main__":
    """
    Run the Flask development server.
    """
    app.run()
