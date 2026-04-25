import os
from dotenv import load_dotenv
from groq import Groq

# Load env
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Load prompt
with open("prompts/describe_prompt.txt", "r") as f:
    prompt_template = f.read()

# Test inputs
test_inputs = [
    "Factory dumping waste into river",
    "Company using solar panels",
    "No employee safety measures",
    "Recycling plastic materials",
    "High carbon emissions from transport"
]

for i, input_text in enumerate(test_inputs):
    prompt = prompt_template.replace("{input_text}", input_text)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    print(f"\nTest Case {i+1}:")
    print(response.choices[0].message.content)