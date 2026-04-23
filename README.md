# Sustainability Compliance Monitor

A tool-based AI solution to monitor and ensure sustainability compliance.

## Project Progress

### 📅 Day 1
* Set up project folders and basic structure.
* Configured API keys and environment variables (.env).
* Initialized Git for version control.
* Verified the initial connection to the Groq AI API.

### 📅 Day 2
* Developed a robust and reusable GroqClient.
* Added error handling and automatic retries for better reliability.
* Integrated logging to track service performance.
* Created test scripts to verify AI responses and client stability.

### 📅 Day 3
* Built a Flask API with a POST endpoint (`/api/analyze`) for AI analysis.
* Implemented `flask-limiter` for rate limiting (30 requests/minute).
* Added security features to strip HTML and block prompt injection.
* Configured specialized system prompts for sustainability compliance expertise.
### ?? Day 4
* Developed AiServiceClient.java using Spring RestTemplate.
* Configured a 10-second timeout for robust service communication.
* Implemented fail-safe error handling (returns null on failure).
* Created a Maven project structure for the Java client.

* Added AiServiceClientStandard.java for instant running without Maven dependencies.
* Provided run_standard_client.bat to bypass 'command not found' errors by using the built-in Java path.
