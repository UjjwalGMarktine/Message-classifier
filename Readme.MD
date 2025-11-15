



Hi, TO use this application. first of all you have to generate a access_token.

** Command to build App container: sudo docker compose build
** Command to build App container: sudo docker compose up

** To generate access_token: You can generate access token using api .
-->> api_endpoint: generate-access-token

** Once you get the token now you are able to access all the APIs .

** Health API: Which tells about our application's health.

** Classify-comments: This api use to classify comments. this will give you response like this: 
-->> api_endpoint: classify-comments/
{
    "status": true,
    "label": "safe",
    "confidence": 0.5488225221633911
}

** Update-models: Using this api you can update NLP models according to your need.
-->> api_endpoint: classify-comments/


**** I have attached postman collection.json file which you import in your postman and can user APIs.