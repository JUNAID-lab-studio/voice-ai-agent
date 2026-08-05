import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Set voice speed
engine.setProperty("rate", 170)

# Set volume
engine.setProperty("volume", 1.0)


def speak(text):
    """
    Convert text to speech.
    """
    print(f"\nAI: {text}\n")
    engine.say(text)
    engine.runAndWait()


def listen():
    """
    Listen to user's voice and convert it to text.
    """
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\n🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(source, timeout=10)

            print("Processing...")

            text = recognizer.recognize_google(audio)

            print(f"You: {text}")

            return text

        except sr.WaitTimeoutError:
            return None

        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand you.")
            return None

        except sr.RequestError:
            speak("Speech recognition service is unavailable.")
            return None
