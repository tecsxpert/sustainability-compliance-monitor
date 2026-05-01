from datetime import datetime

def fallback_describe():
    return {
        "title": "Basic Sustainability Analysis",
        "summary": "AI service unavailable. Showing fallback response.",
        "overview": "The system could not process AI insights at this moment.",
        "generated_at": str(datetime.now())
    }

def fallback_recommend():
    return [
        {
            "action_type": "General",
            "description": "Adopt sustainable practices such as reducing waste and energy usage.",
            "priority": "Medium"
        }
    ]

def fallback_report():
    return {
        "title": "Fallback Sustainability Report",
        "summary": "AI report generation failed.",
        "overview": "This is a fallback report due to AI service issue.",
        "key_items": [],
        "recommendations": [],
        "generated_at": str(datetime.now())
    }