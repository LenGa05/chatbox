"""Casanova Electrical chatbot logic and optional CLI entrypoint."""
from __future__ import annotations
import textwrap
from dataclasses import dataclass

@dataclass
class Intent:
    """Represents a simple keyword driven chatbot intent."""
    keywords: set[str]
    response: str

class ElectricCompanyChatBot:
    """Rule-based chatbot tuned for Casanova Electrical."""

    def __init__(self) -> None:
        self._intents: list[Intent] = [
            Intent(
                keywords={"outage", "emergency", "urgent", "no power", "sparks"},
                response=textwrap.dedent("""
                    If you're facing an urgent electrical issue, please call Casanova
                    Electrical right away and then submit the emergency details at
                    https://casanovaelectrical.com/contact/. We'll dispatch a licensed
                    electrician as quickly as possible.
                """).strip(),
            ),
            Intent(
                keywords={"quote", "estimate", "pricing", "cost", "bid"},
                response=textwrap.dedent("""
                    We'd be happy to prepare a customized estimate. Share the project
                    details through https://casanovaelectrical.com/contact/ and our
                    office will follow up with pricing and scheduling options.
                """).strip(),
            ),
            Intent(
                keywords={"services", "panel", "lighting", "ev", "install"},
                response=textwrap.dedent("""
                    Casanova Electrical handles residential and commercial work
                    including panel upgrades, lighting design, EV charger installs,
                    and preventive maintenance. Let us know what you need at
                    https://casanovaelectrical.com/services/.
                """).strip(),
            ),
            Intent(
                keywords={"license", "insured", "bonded", "certified"},
                response=textwrap.dedent("""
                    Our electricians are fully licensed, insured, and code compliant.
                    If you need documentation for a permit or project, contact the
                    office team via https://casanovaelectrical.com/contact/.
                """).strip(),
            ),
        ]
        self._fallback_response = (
            "I'm here to help! Please share a few details about your project or use "
            "https://casanovaelectrical.com/contact/ to reach the Casanova Electrical "
            "team directly."
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
    bot = ElectricCompanyChatBot()
    print("Welcome to Casanova Electrical's virtual assistant! Type 'quit' to exit.\n")

    while True:
        try:
            user_message = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print("\nThanks for chatting with Casanova Electrical. Goodbye!")
            break

        if user_message.strip().lower() in {"quit", "exit"}:
            print("Thanks for chatting with Casanova Electrical. Goodbye!")
            break

        response = bot.get_response(user_message)
        print(f"CasanovaBot: {response}\n")

if __name__ == "__main__":
    run_chat()

