from speech import listen, speak

speak("Voice agent is ready.")

while True:
    text = listen()

    if text is None:
        continue

    if text.lower() in ["exit", "quit", "stop"]:
        speak("Goodbye.")
        break

    speak(f"You said {text}")
