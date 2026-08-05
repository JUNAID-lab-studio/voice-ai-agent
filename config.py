import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL = os.getenv("MODEL", "llama-3.3-70b-versatile")

SYSTEM_PROMPT = """
You are a helpful Voice AI Assistant.

Rules:
1. Keep responses short and natural.
2. Be polite and friendly.
3. If you don't know something, say so honestly.
4. Answer in clear English.
"""
