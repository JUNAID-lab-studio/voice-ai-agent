import speech_recognition as sr
import pyttsx3
from groq import Groq
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

engine = pyttsx3.init()
engine.setProperty("rate", 170)

recognizer = sr.Recognizer()

SYSTEM_PROMPT = """
You are a helpful Voice AI Assistant.
Answer briefly and clearly.
"""

def speak(text):
    print("AI:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You:", text)
        return text
    except:
        return ""

while True:
    question = listen()

    if question == "":
        continue

    if question.lower() in ["exit", "quit", "stop"]:
        speak("Goodbye!")
        break

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question}
        ]
    )

    answer = response.choices[0].message.content
    speak(answer)
