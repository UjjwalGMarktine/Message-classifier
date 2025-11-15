



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

