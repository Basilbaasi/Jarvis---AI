from jarvis.core import *
from jarvis.commands import *

def greet():
    import datetime
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning, sir.")
    elif 12 <= hour < 18:
        speak("Good afternoon, sir.")
    else:
        speak("Good evening, sir.")
    speak("Welcome back.")

if __name__ == "__main__":
    greet()
    while True:
        print("\n- Speak chat for a chat version\n- For searching web specify that like in web\n- Include jarvis in speach for AI answer\n- Include jarvis full in speach for AI answer in detail\n")
        query = listen()
        if query == "none":
            continue

        if 'wikipedia' in query:
            search_wikipedia(query)

        elif 'jarvis' in query:
            if 'full' in query:
                answer_question_full(query)
            else:
                answer_question_short(query)

        elif 'sleep' in query:
            speak("Sleeping for 5 minutes...")
            import time
            time.sleep(300)

        elif 'chat' in query:
            chat()

        elif any(k in query for k in ['open', 'close']):
            control_apps(query)

        elif 'on web' in query or 'in web' in query:
            open_website(query)

        elif 'open yt' in query or 'open movies' in query or 'open edge' in query:
            open_path(query)

        elif 'time' in query:
            tell_time()

        elif 'your name' in query or 'who are you' in query:
            respond_identity()

        elif any(exit_word in query for exit_word in ['exit', 'get lost']):
            speak("Okay, goodbye sir.")
            break
