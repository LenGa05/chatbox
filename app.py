"""Flask web application exposing the Casanova Electrical chatbot."""
from __future__ import annotations
from flask import Flask, jsonify, render_template, request
from chatbot import ElectricCompanyChatBot

def create_app() -> Flask:
    """Create and configure the Flask application."""
    app = Flask(__name__)
    bot = ElectricCompanyChatBot()

    @app.get("/")
    def index() -> str:
        return render_template("index.html")

    @app.post("/api/chat")
    def chat() -> tuple[dict[str, str], int]:
        payload = request.get_json(silent=True) or {}
        message = str(payload.get("message", ""))
        response = bot.get_response(message)
        return jsonify({"reply": response}), 200

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

