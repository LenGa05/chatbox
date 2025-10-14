# Casanova Electrical Chat Assistant

This project delivers a lightweight virtual assistant tailored for
[Casanova Electrical](https://casanovaelectrical.com/). The chatbot can run in two
modes:

1. **Website widget** powered by a Flask backend and a modern, responsive UI.
2. **Command-line helper** for quick local testing of conversation flows.

The response logic is intentionally simple so you can adapt the answers to your
team's workflows without retraining any AI models.

## Requirements

- Python 3.10 or newer
- Optional: Node/npm only if you plan to bundle the static assets yourself (not
  required for the default setup)

Install the Python dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run the web chatbot

```bash
flask --app app.py run --debug
```

Then open <http://127.0.0.1:5000>. The chat widget posts messages to the
`/api/chat` endpoint, which reuses the rule-based responses defined in
`chatbot.py`.

### Deploying on casanovaelectrical.com

1. Copy `static/` and `templates/` into your website project. If you're using a
   CMS, embed the HTML from `templates/index.html` inside the desired page and
   include the CSS/JS assets.
2. Host the Flask app (or any Python WSGI server) wherever you prefer, and point
   the form's `fetch('/api/chat')` URL to that deployment.
3. Edit the responses inside `ElectricCompanyChatBot` to match your specific
   services, phone numbers, or booking links.

## Run the CLI chatbot

```bash
python chatbot.py
```

Type your questions into the prompt. Enter `quit` or `exit` (or press
`Ctrl+C`) to end the session.

## Tests

```bash
pytest
```
