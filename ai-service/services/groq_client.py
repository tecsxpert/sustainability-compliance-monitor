from dotenv import load_dotenv
load_dotenv()

import os
from groq import Groq

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is not set. Check your .env file")

client = Groq(api_key=api_key)

def call_groq(prompt):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
            max_tokens=500
        )

        return response.choices[0].message.content

    except Exception as e:
        print(f"[ERROR] Groq API failed: {e}")
        raise