from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import fasttext, re, threading, jwt
from .training import train_model
from comment_classification.jwt_utils import auth_token
from datetime import datetime, timedelta, UTC


@api_view(['GET'])
def health_check(request):
    return Response({"status": True, "message": "Application health is good"})


def normalize_text(text: str) -> str:
    print(text)
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)
    return text

@auth_token
@api_view(['POST'])
def classify_comments(request):
    try: 
        text = request.data.get("text")
        err_data = {"status": False}
        print("text: ", text)
        if not text: 
            err_data["message"] = "Please provide text."
            err_data["error_code"] = 1
            return Response(err_data, status=400)

        text = normalize_text(text)

        model = fasttext.load_model(settings.MODEL_PATH)
        labels, probs = model.predict(text, k=1)
        print("labels:", labels, probs, float(probs[0]))

        response = {
            "status": True,
            "label": labels[0].replace("__label__", ""),
            "confidence": float(probs[0])
        }
        return Response(response)
    except Exception as e:
        return Response({"status": False, "message": str(e)}, status=400)
    

@auth_token
@api_view(['POST'])
def update_dataset(request):
    data_set_file = request.FILES.get("data_set_file")
    if not data_set_file:
        return Response({"status": False, "message": "Please provide data_set_file"}, status=400)

    file_content = data_set_file.read()
    print("File: ", data_set_file.name)
    print("Size:", len(file_content))

    threading.Thread(
        target=train_model.train_model_view,
        kwargs={"file_bytes": file_content},
        daemon=True
    ).start()

    return Response({"status": True, "message": "Training started in background."})


@api_view(['GET'])
def generate_access_token(request):
    now = datetime.now(UTC)

    payload = {
        "user_id": "1234",
        "exp": now + timedelta(hours=2),
        "iat": now
    }

    token = jwt.encode(
        payload,
        "read.ai",
        algorithm="HS256"
    )
    return Response({"status": True, "message": "Token get successfully.", "access_token": token})
