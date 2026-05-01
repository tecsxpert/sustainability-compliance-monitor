import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
import traceback
import json

# Load .env
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

api_key = os.getenv("GROQ_API_KEY")

print(" GROQ_API_KEY loaded:", "YES" if api_key else "NO")

if not api_key:
    raise ValueError("GROQ_API_KEY not found")

client = Groq(api_key=api_key)


def call_groq(messages, fallback_function):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",   #  correct model
            messages=messages,
            temperature=0.3,
            max_tokens=300
        )

        raw_output = response.choices[0].message.content

        #  Try parsing JSON safely
        try:
            parsed_output = json.loads(raw_output)
        except Exception:
            parsed_output = {
                "raw_text": raw_output
            }

        return {
            "data": parsed_output,
            "is_fallback": False
        }

    except Exception as e:
        print("\n GROQ ERROR START ")
        traceback.print_exc()
        print(" GROQ ERROR END \n")

        return {
            "data": fallback_function(),
            "is_fallback": True
        }