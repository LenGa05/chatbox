from pathlib import Path
import sys

# Ensure the project root is importable when tests are executed from any directory.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from chatbot import ElectricCompanyChatBot


def test_emergency_response_points_to_contact_page():
    bot = ElectricCompanyChatBot()
    response = bot.get_response("I think there is a power outage in my area")
    assert "contact" in response.lower()
    assert "https://casanovaelectrical.com/contact/" in response


def test_empty_message_prompts_user():
    bot = ElectricCompanyChatBot()
    response = bot.get_response("   ")
    assert "please enter" in response.lower()


def test_unknown_question_uses_fallback():
    bot = ElectricCompanyChatBot()
    response = bot.get_response("What is the meaning of life?")
    assert "casanova electrical" in response.lower()
    assert "contact" in response.lower()
