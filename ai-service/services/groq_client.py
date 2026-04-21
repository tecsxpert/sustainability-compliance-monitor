import os
import time
import logging
from groq import Groq
from dotenv import load_dotenv

# Set up logging for Day 2
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

class GroqClient:
    def __init__(self, model="llama-3.1-8b-instant"):
        self.api_key = os.getenv("GROQ_API_KEY")
        if not self.api_key:
            logger.error("GROQ_API_KEY is missing!")
            raise ValueError("GROQ_API_KEY not found")
        
        self.client = Groq(api_key=self.api_key)
        self.model = model

    def get_completion(self, prompt, retries=3):
        """
        AI Call with 3-retry logic, exponential backoff, and JSON parsing.
        """
        for attempt in range(retries):
            try:
                logger.info(f"AI Call Attempt {attempt + 1}...")
                
                # Enforce JSON if requested in prompt
                response_format = {"type": "json_object"} if "json" in prompt.lower() else None
                
                chat_completion = self.client.chat.completions.create(
                    messages=[{"role": "user", "content": prompt}],
                    model=self.model,
                    response_format=response_format
                )
                
                logger.info("AI Call Successful!")
                return chat_completion.choices[0].message.content
                
            except Exception as e:
                logger.warning(f"Attempt {attempt + 1} failed: {e}")
                if attempt < retries - 1:
                    wait_time = 2 ** attempt  # Exponential backoff (1s, 2s, 4s...)
                    logger.info(f"Waiting {wait_time} seconds before retrying...")
                    time.sleep(wait_time)
                else:
                    logger.error("All 3 attempts failed!")
                    raise e
