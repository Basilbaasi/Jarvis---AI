# 🤖 Jarvis AI Assistant

**Jarvis** is a modular voice-controlled Python AI assistant powered by NVIDIA's DeepSeek-R1 LLM. It supports speech recognition, app automation, Wikipedia search, web browsing, and real-time conversation.

---

## 🧠 Features

- 🎙️ Voice control using microphone input
- 🧾 Wikipedia summary lookup
- 🧠 Real-time LLM responses (DeepSeek)
- 🗂️ Open/close installed apps by voice
- 🌐 Web search via Bing
- 🎧 Media playback & file explorer automation
- 🗨️ Chat mode using DeepSeek LLM

---

## ⚙️ Tech Stack

| Component       | Description                                      |
|----------------|--------------------------------------------------|
| Python          | Core logic                                       |
| SpeechRecognition | Voice input                                  |
| pyttsx3         | Text-to-speech (offline)                         |
| AppOpener       | App automation on Windows                        |
| wikipedia       | Query Wikipedia summaries                        |
| openai SDK      | Used with NVIDIA DeepSeek API                    |
| python-dotenv   | Secure environment variable loading              |

---

## 🔐 API Integration

This assistant uses the **NVIDIA DeepSeek-R1** model.

> 🔗 [View Model on NVIDIA Build Platform](https://build.nvidia.com/deepseek-ai/deepseek-r1-0528)

To use it:

1. Sign up at [https://build.nvidia.com](https://build.nvidia.com)
2. Get your API key
3. Create a `.env` file in your root directory:

```env
OPENAI_API_KEY=your_nvidia_key_here
📦 Installation
bash
Copy
Edit
git clone https://github.com/Basilbaasi/Jarvis---AI.git
cd Jarvis---AI
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
🚀 Run the Assistant
bash
Copy
Edit
python main.py
Say commands like:

“Jarvis open YouTube”

“Jarvis what is machine learning”

“Jarvis play music”

“Jarvis search pandas in web”

📄 License
MIT License (add your preferred license if applicable).

✨ Credits
Built with 💻 by Basil
Powered by DeepSeek-R1 on NVIDIA's developer platform.