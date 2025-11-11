const chatLog = document.querySelector('#chat-log');
const chatForm = document.querySelector('#chat-form');
const chatInput = document.querySelector('#chat-input');

const templates = {
  message({ author, text, tone }) {
    const li = document.createElement('li');
    li.className = `chat-message chat-message--${tone}`;

    const avatar = document.createElement('span');
    avatar.className = 'chat-message__avatar';
    avatar.textContent = author;

    const bubble = document.createElement('div');
    bubble.className = 'chat-message__bubble';
    bubble.textContent = text;

    li.appendChild(avatar);
    li.appendChild(bubble);
    return li;
  },
};

function appendMessage({ author, text, tone }) {
  const messageNode = templates.message({ author, text, tone });
  chatLog.appendChild(messageNode);
  chatLog.scrollTo({ top: chatLog.scrollHeight, behavior: 'smooth' });
}

async function sendMessage(event) {
  event.preventDefault();
  const message = chatInput.value.trim();
  if (!message) return;

  appendMessage({ author: 'You', text: message, tone: 'user' });
  chatInput.value = '';
  chatInput.focus();

  const response = await fetch('/api/chat', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ message }),
  });

  if (!response.ok) {
    appendMessage({
      author: 'Bot',
      text: 'Sorry, something went wrong while reaching the server. Please try again.',
      tone: 'bot',
    });
    return;
  }

  const data = await response.json();
  appendMessage({ author: 'Bot', text: data.reply, tone: 'bot' });
}

chatForm.addEventListener('submit', sendMessage);

appendMessage({
  author: 'Bot',
  text: "Hi! I'm the Casanova Electrical assistant. How can I help you today?",
  tone: 'bot',
});

