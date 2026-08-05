# Voice AI Agent

## Description
This is a Python-based Voice AI Agent that can:
- Listen to voice commands
- Convert speech to text
- Respond using text-to-speech

## Requirements
- Python 3.10+
- speechrecognition
- pyttsx3
- pyaudio

## Run

```bash
pip install -r requirements.txt
python speech.py

## Trade-offs

- Uses speech recognition for voice input.
- Uses text-to-speech for responses.
- Basic command-line interface.
- Future improvements:
- Better speech accuracy.
- Support for multiple languages.
- More intelligent conversations using a larger AI model.

## Sample Inputs and Outputs

### Example 1
**Input:**
Hello

**Output:**
Hello! How can I help you today?

---

### Example 2
**Input:**
What is Python?

**Output:**
Python is a high-level programming language used for web development, AI, automation, and data science.

---

### Example 3
**Input:**
Tell me a joke.

**Output:**
Why do programmers prefer dark mode?
Because light attracts bugs!

---

### Example 4
**Input:**
What is today's date?

**Output:**
Today's date is displayed according to your system date.

---

### Example 5
**Input:**
Goodbye

**Output:**
Goodbye! Have a great day.

