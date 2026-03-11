"""Mora Plumbing LLC chatbot logic and optional CLI entrypoint."""
from __future__ import annotations
import textwrap
from dataclasses import dataclass

@dataclass
class Intent:
    """Represents a simple keyword driven chatbot intent."""
    keywords: set[str]
    response: str

class PlumbingCompanyChatBot:
    """Rule-based chatbot tuned for Mora Plumbing LLC."""

    def __init__(self) -> None:
        self._intents: list[Intent] = [
            Intent(
                keywords={"leak", "burst", "emergency", "water damage"},
                response=textwrap.dedent("""
                    If you have a plumbing emergency, call Mora Plumbing LLC right away
                    at (419) 555-0123. We serve homes and businesses throughout the
                    Paulding area and can help with urgent leaks and pipe issues.
                """).strip(),
            ),
            Intent(
                keywords={"quote", "estimate", "pricing", "cost", "service"},
                response=textwrap.dedent("""
                    We'd be glad to provide an estimate. Share your plumbing issue,
                    location, and preferred schedule, and our team will follow up with
                    transparent pricing.
                """).strip(),
            ),
            Intent(
                keywords={"drain", "clog", "toilet", "sink", "sewer"},
                response=textwrap.dedent("""
                    We handle clogged drains, sewer backups, and fixture blockages.
                    Mora Plumbing LLC uses safe, effective methods to restore flow fast.
                """).strip(),
            ),
            Intent(
                keywords={"water heater", "tankless", "install", "replace"},
                response=textwrap.dedent("""
                    We install and service both standard and tankless water heaters.
                    If your system is leaking or not heating properly, we can help.
                """).strip(),
            ),
        ]
        self._fallback_response = (
            "Thanks for reaching out to Mora Plumbing LLC. Tell us a little about your "
            "plumbing project in the Paulding area, and we'll point you in the right "
            "direction."
        )

    def get_response(self, message: str) -> str:
        """Return a chatbot response for the provided *message*."""
        normalized = message.strip().lower()
        if not normalized:
            return "Please enter a question so I can help you."

        for intent in self._intents:
            if any(keyword in normalized for keyword in intent.keywords):
                return intent.response
        return self._fallback_response

def run_chat() -> None:
    """Launch the chatbot in interactive console mode."""
    bot = PlumbingCompanyChatBot()
    print("Welcome to Mora Plumbing LLC's virtual assistant! Type 'quit' to exit.\n")

    while True:
        try:
            user_message = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print("\nThanks for chatting with Mora Plumbing LLC. Goodbye!")
            break

        if user_message.strip().lower() in {"quit", "exit"}:
            print("Thanks for chatting with Mora Plumbing LLC. Goodbye!")
            break

        response = bot.get_response(user_message)
        print(f"MoraBot: {response}\n")

if __name__ == "__main__":
    run_chat()
