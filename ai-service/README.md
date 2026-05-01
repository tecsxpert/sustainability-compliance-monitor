# AI Service — Sustainability Compliance Monitor

This service handles all AI functionalities using **Flask + Groq API**.

---

## Features

* AI-powered description generation
* Sustainability recommendations
* Full compliance report generation
* Health monitoring endpoint
* Fallback handling if AI fails

---

## Tech Stack

* Python 3.11
* Flask
* Groq API (LLaMA 3)
* Redis (for caching)
* Flask-Limiter (rate limiting)

---

## Folder Structure

ai-service/
│── routes/
│── services/
│── prompts/
│── app.py
│── requirements.txt

---

## Setup Instructions

### 1. Clone Repository

git clone https://github.com/maash1408/sustainability-compliance-monitor.git
cd Sustainability-Compliance-Monitor/ai-service

---

### 2. Create Virtual Environment

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

---

### 3. Install Dependencies

pip install -r requirements.txt

---

### 4. Environment Variables

Create `.env` file:

GROQ_API_KEY=your_api_key
REDIS_URL=redis://localhost:6379

---

## Run the Service

python app.py

App will run on:

http://localhost:5000

---

## API Endpoints

---

### 1. POST /describe

Generates sustainability description.

Request:
{
"company": "ABC Corp",
"data": "Reduced emissions but lacks waste policy"
}

Response:
{
"title": "Sustainability Overview",
"summary": "Company shows progress...",
"generated_at": "timestamp"
}

---

### 2. POST /recommend

Returns recommendations.

Request:
{
"data": "High emissions and waste issues"
}

Response:
[
{
"action_type": "Emission Reduction",
"description": "Switch to renewable energy",
"priority": "High"
}
]

---

### 3. POST /generate-report

Generates full report.

Request:
{
"data": "Company sustainability data"
}

Response:
{
"title": "Report",
"summary": "...",
"overview": "...",
"key_items": [],
"recommendations": []
}

---

## Health Endpoint

GET /health

Response:
{
"status": "OK",
"model": "llama3",
"uptime": "2h",
"avg_response_time": "1.2s"
}

---

## Error Handling

* Groq failures return fallback response
* No server crash on AI failure

Example:
{
"is_fallback": true,
"message": "AI unavailable"
}

---

## Security

* Rate limit: 30 requests/min
* Input validation
* Prompt injection protection

---

## Docker

Build:
docker build -t ai-service .

Run:
docker run -p 5000:5000 ai-service

---

## Performance

* Response time < 2 seconds
* Cached responses faster

---

## Developer Notes

* All responses are JSON formatted
* AI calls handled with try-catch
* Fallback implemented

---
