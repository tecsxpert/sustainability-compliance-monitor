import json
from services.groq_client import call_groq

def generate_recommendations(input_text):
    try:
        with open("prompts/recommend_prompt.txt", "r") as f:
            prompt_template = f.read()

        prompt = prompt_template.replace("{input_text}", input_text)

        # 🔥 THIS IS WHERE STEP 2 CODE GOES
        response = call_groq(prompt)

        print("RAW RESPONSE:", response)

        # ✅ CLEAN RESPONSE
        cleaned = response.strip() \
            .replace("```json", "") \
            .replace("```", "")

        # ✅ CONVERT TO JSON
        parsed = json.loads(cleaned)

        return parsed   # ✅ NOW RETURNS ARRAY (CORRECT)

    except Exception as e:
        print("ERROR:", e)

        return [
            {
                "action_type": "General",
                "description": "Review manually",
                "priority": "MEDIUM"
            }
        ]