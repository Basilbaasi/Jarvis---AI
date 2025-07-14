import os
import time
import wikipedia
import webbrowser
from datetime import datetime
from jarvis.core import speak
from jarvis.config import client
from AppOpener import open as open_app, close as close_app


# ─────────────────────────────────────────────
#  AI AND WIKIPEDIA
# ─────────────────────────────────────────────

def search_wikipedia(query: str):
    query = query.replace("wikipedia", "").strip()
    speak("Searching Wikipedia...")
    try:
        summary = wikipedia.summary(query, sentences=2)
        print(summary)
        speak(summary)
    except Exception as e:
        print(f"Wikipedia Error: {e}")
        speak("Sorry, I couldn't find anything useful.")


def answer_question_short(question: str):
    question = question.replace("jarvis", "").strip()
    try:
        completion = client.chat.completions.create(
            model="nvidia/nemotron-4-340b-instruct",
            messages=[{"role": "user", "content": question}],
            temperature=0.2,
            top_p=0.7,
            max_tokens=350,
            stream=True
        )
        response_text = ""
        for chunk in completion:
            content = chunk.choices[0].delta.content
            if isinstance(content, str):
                response_text += content
        response_text = response_text.replace("*", " ")
        print(response_text[:350])
        speak(response_text[:350])
    except Exception as e:
        print("AI Error (short):", e)
        speak("I'm sorry, I couldn't find an answer.")
def chat():
    while True:
        question = input("enter for ai help :  ")
        try:
            completion = client.chat.completions.create(
                model="nvidia/llama-3.1-nemotron-70b-instruct",
                messages=[{"role": "user", "content": question}],
                temperature=0.5,
                top_p=1,
                max_tokens=1024,
                stream=True
            )
            response_text = ""
            for chunk in completion:
                content = chunk.choices[0].delta.content
                if isinstance(content, str):
                    response_text += content
            response_text = response_text.replace("*", " ").replace("###", " ")
            print("result:\n\n\n", response_text)
            speak("answer")
            p = input("\n\n\nREAD Y/N : ")
            if p == "y":
                speak(response_text)
        except Exception as e:
            print("An error occurred:", e)
            speak("I'm sorry, I couldn't find an answer.")



def answer_question_full(question: str):
    question = question.replace("jarvis", "").strip()
    try:
        completion = client.chat.completions.create(
            model="nvidia/nemotron-4-340b-instruct",
            messages=[{"role": "user", "content": question}],
            temperature=0.2,
            top_p=0.7,
            max_tokens=1024,
            stream=True
        )
        response_text = ""
        for chunk in completion:
            content = chunk.choices[0].delta.content
            if isinstance(content, str):
                response_text += content
        response_text = response_text.replace("*", " ").replace("###", " ")
        print("result:\n\n\n", response_text)
        speak(response_text)
    except Exception as e:
        print("AI Error (full):", e)
        speak("I'm sorry, I couldn't find an answer.")


# ─────────────────────────────────────────────
#  OPEN/CLOSE APPS BY NAME
# ─────────────────────────────────────────────

def control_apps(command: str):
    command = command.lower()
    apps = {
        "youtube": "youtube",
        "whatsapp": "whatsapp",
        "instagram": "instagram",
        "telegram": "telegram",
        "vlc": "vlc media player",
        "media player": "media player",
        "vs": "visual studio code",
        "store": "microsoft store",
        "settings": "settings",
        "notes": "onenote",
        "lightroom": "adobe lightroom",
        "photoshop": "adobe photoshop",
        "pc manager": "pc manager",
    }

    for key, app in apps.items():
        if f"open {key}" in command:
            open_app(app)
            speak(f"Opening {key}")
            return
        elif f"close {key}" in command:
            close_app(app)
            speak(f"Closing {key}")
            return

    # Generic close phrases
    if any(kw in command for kw in ["exit", "close", "get lost", "poda"]):
        speak("Okay then. Bye sir.")
        close_app("python")


# ─────────────────────────────────────────────
#  WEB SEARCH
# ─────────────────────────────────────────────

def open_website(query: str):
    query = query.replace("in web", "").replace("on web", "").strip()
    url = f"https://www.bing.com/search?q={query}"
    webbrowser.open(url)
    speak("Searching the web.")


# ─────────────────────────────────────────────
#  CUSTOM FILE/FOLDER SHORTCUTS
# ─────────────────────────────────────────────

def open_path(query: str):
    # Hardcoded paths based on your setup
    known_paths = {
        "open yt": "E:\\Yutb download",
        "open edge": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        "open movies": "D:\\movies",
        "open downloads": "C:\\Users\\Admin\\Downloads",
        "open premiere": "C:\\Program Files\\Adobe\\Adobe Premiere Pro 2023",
    }

    for trigger, path in known_paths.items():
        if trigger in query:
            try:
                os.startfile(path)
                speak("Opening...")
                return
            except Exception as e:
                print(f"Failed to open {path}: {e}")
                speak("Unable to open the specified path.")
                return


# ─────────────────────────────────────────────
#  TIME + IDENTITY
# ─────────────────────────────────────────────

def tell_time():
    current_time = datetime.now().strftime("%I:%M:%S")
    speak(f"Sir, the time is {current_time}")


def respond_identity():
    speak("I am jarvis AI, a personal assistant for Basil. I can open apps, search the web, and answer your questions.")

