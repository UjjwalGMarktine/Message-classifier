import jwt
from rest_framework.response import Response
from django.conf import settings
from datetime import datetime, timedelta, timezone, UTC
from functools import wraps
from rest_framework.renderers import JSONRenderer


def generate_access_token(user_id):
    now = datetime.now(UTC)

    payload = {
        "user_id": user_id,
        "exp": now + settings.JWT_SETTINGS["ACCESS_TOKEN_LIFETIME"],
        "iat": now
    }

    token = jwt.encode(
        payload,
        "read.ai",
        algorithm="HS256"
    )
    return token


def auth_token(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):

        def error(message, status_code):
            response = Response(
                {"status": False, "message": message},
                status=status_code
            )
            response.accepted_renderer = JSONRenderer()
            response.accepted_media_type = "application/json"
            response.renderer_context = {}
            return response

        auth_header = request.headers.get("Authorization")
        if not auth_header: return error("Authorization header missing", 401)
        if not auth_header.startswith("Bearer "): return error("Invalid Authorization format", 401)
        token = auth_header.split(" ")[1]

        try:
            payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=["HS256"])

            issued_at = payload.get("iat")
            if not issued_at: return error("Token missing issued time", 401)

            issued_time = datetime.fromtimestamp(issued_at, tz=timezone.utc)
            now = datetime.now(timezone.utc)

            if now - issued_time > timedelta(hours=2): return error("Token expired (2-hour limit)", 401)
            request.user_id = payload.get("user_id")

        except jwt.ExpiredSignatureError: return error("Token expired", 401)
        except jwt.InvalidTokenError: return error("Invalid token", 401)
        return func(request, *args, **kwargs)
    return wrapper
