# Jarvis AI Assistant

**Jarvis** is a modular, voice-controlled desktop AI assistant built in Python. It listens to your commands, responds with natural voice, can control installed apps, search the web, answer general questions using LLMs (like NVIDIA Nemotron), and more — all hands-free.

---

## 🧠 Features

- 🎙️ Voice interaction using `speech_recognition` and `pyttsx3`
- 📚 Wikipedia summary fetching
- 💬 AI-powered answers (NVIDIA Nemotron via OpenAI SDK)
- ⚙️ Open/close system apps like YouTube, WhatsApp, VLC, etc.
- 🌐 Bing-based web search
- 🧩 Modular code architecture (clean separation of logic)
- 🕒 Tells current time, responds to personal questions

---

## 🗂️ Folder Structure

jarvis-ai/
├── main.py # Main voice loop
├── requirements.txt # Python dependencies
├── .env # API keys
├── .gitignore # Ignored files/folders
├── README.md # This file
└── jarvis/ # Core package
├── init.py
├── core.py # Speak/listen logic
├── config.py # OpenAI config loader
└── commands.py # Wikipedia, AI answers, app control etc.

yaml
Copy
Edit

---

## ⚙️ Setup Instructions

### 1. Clone this repo:
```bash
git clone https://github.com/YOUR_USERNAME/jarvis-ai.git
cd jarvis-ai
2. Install dependencies:
Make sure you're using Python 3.11.

bash
Copy
Edit
pip install -r requirements.txt
3. Configure API key:
Create a .env file:

ini
Copy
Edit
OPENAI_API_KEY=your_nvidia_integrate_key_here
4. Run the assistant:
bash
Copy
Edit
python main.py
📦 Dependencies
speechrecognition

pyttsx3

wikipedia

openai

AppOpener

python-dotenv

Install with:

bash
Copy
Edit
pip install -r requirements.txt
🧠 AI Integration
Jarvis connects to NVIDIA’s Nemotron LLM via OpenAI-compatible API (NVIDIA Cloud Foundry or Integrate).
You can use any compatible endpoint that works with the OpenAI Python SDK.

👤 Author
Basil – Python Developer & AI/ML Engineer

This project is built purely in Python 3.11 and modularized for clarity and expansion. Future plans include browser automation, emotion-driven response handling, and GUI-based trigger input.

📜 License
This project is open source and available under the MIT License.