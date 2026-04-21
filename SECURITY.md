# SECURITY.md - Tool-65 Sustainability Compliance Monitor

## AI Service Threat Model

As the **AI Developer 2**, I have identified the following 5 primary security threats to our AI microservice:

1.  **Prompt Injection**: Malicious users may attempt to bypass compliance rules by providing "ignore all previous instructions" commands.
2.  **API Key Exposure**: Risks associated with leaking the `GROQ_API_KEY` through logs or unencrypted storage.
3.  **Denial of Service (DoS)**: High-frequency requests aimed at draining the API quota and increasing operational costs.
4.  **Sensitive Data Leakage**: Users inputting private corporate data that is then sent to external LLM providers without anonymization.
5.  **Output Injection (XSS)**: Malicious AI responses being rendered in the web UI without proper sanitization, leading to security breaches.

## Mitigation Strategies
- [x] Implemented .env protection (Day 1)
- [x] Implemented Robust Client with error handling (Day 2)
- [ ] Planned: Input Sanitization middleware (Day 3)
- [ ] Planned: Flask Rate Limiter (Day 3)
