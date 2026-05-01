import os

# Get absolute path of current file (config.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build correct path to prompts folder
PROMPTS_DIR = os.path.join(BASE_DIR, "prompts")

# Load prompts safely
with open(os.path.join(PROMPTS_DIR, "describe_prompt.txt"), encoding="utf-8") as f:
    DESCRIBE_PROMPT = f.read()

with open(os.path.join(PROMPTS_DIR, "recommend_prompt.txt"), encoding="utf-8") as f:
    RECOMMEND_PROMPT = f.read()

with open(os.path.join(PROMPTS_DIR, "generate_report.txt"), encoding="utf-8") as f:
    REPORT_PROMPT = f.read()