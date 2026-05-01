from groq import Groq
from dotenv import load_dotenv
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

r = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[{"role": "user", "content": "Say hello"}],
)

print(r.choices[0].message.content)