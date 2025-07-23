# 🤖 Jarvis AI Assistant

**Jarvis** is a modular voice-controlled Python AI assistant powered by NVIDIA's **Google Gemma 3n-e4b-it** LLM. It supports speech recognition, app automation, Wikipedia search, web browsing, and real-time conversation.

---

## 🧠 Features

- 🎙️ Voice control using microphone input  
- 🧾 Wikipedia summary lookup  
- 🧠 Real-time LLM responses via NVIDIA API (Gemma)  
- 🗂️ Open/close installed apps by voice  
- 🌐 Web search via Bing  
- 🎧 Media playback & file explorer automation  
- 🗨️ Chat mode using NVIDIA-hosted LLM  

---

## ⚙️ Tech Stack

| Component         | Description                                      |
|------------------|--------------------------------------------------|
| Python            | Core logic                                       |
| SpeechRecognition | Voice input                                      |
| pyttsx3           | Text-to-speech (offline)                         |
| AppOpener         | App automation on Windows                        |
| wikipedia         | Query Wikipedia summaries                        |
| requests          | HTTP client to call NVIDIA’s hosted LLMs        |
| python-dotenv     | Secure environment variable loading              |

---

## 🔐 API Integration

This assistant uses the **Google Gemma 3n-e4b-it** model via NVIDIA's developer API.

> 🔗 [View Model on NVIDIA Build Platform](https://build.nvidia.com/google/gemma-3n-e4b-it)

To use it:

1. Sign up at [https://build.nvidia.com](https://build.nvidia.com)
2. Get your API key
3. Create a `.env` file in your root directory:

```env
NVIDIA_API_KEY=your_nvidia_api_key_here
NVIDIA_API_BASE_URL=https://integrate.api.nvidia.com/v1
📦 Installation
bash
Copy
Edit
git clone https://github.com/Basilbaasi/Jarvis---AI.git
cd Jarvis---AI
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
MIT License

✨ Credits
Built with 💻 by Basil
Powered by Google Gemma LLM via NVIDIA's Developer Platform