

Project Requirements:

Develop a Python-based microservice exposing a simple, well-documented REST to receive chat messages and return an abuse classification with confidence scores and labels (abusive, hate speech, harassment, safe).
Integrate rules engine capable of handling multiple languages, slang, and obfuscated text.
Ensure rules/models can be easily updated.
The service must be stateless, horizontally scalable, and optimized for low-latency, real-time processing.
Include logging and monitoring for model performance and system health.
Provide configurable thresholds for flagging/blocking.
Implement strong security practices including authentication, rate limiting, and protection of user data privacy.



Hi, TO use this application. first of all you have to generate a access_token.

** Command to build App container: sudo docker compose build
** Command to build App container: sudo docker compose up

** To generate access_token: we generate access token api .
** Once you get the token now you are able to access all the APIs .

** Health API: Which tells about our application's health.

** classify-comments: This api use to classify comments. this will give you response like this: 
{
    "status": true,
    "label": "safe",
    "confidence": 0.5488225221633911
}

** Update-models: Using this api you can update NLP models according to your need.

