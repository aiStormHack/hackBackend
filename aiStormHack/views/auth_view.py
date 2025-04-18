from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from decouple import config

BASE_URL = config("BASE_URL")


@csrf_exempt
def login_view(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST method allowed"}, status=405)

    try:
        data = json.loads(request.body)
        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            return JsonResponse({"error": "Email and password are required."}, status=400)

        # Forward login request to Ayor's backend
        response = requests.post(f"{BASE_URL}/auth/jwt/create/", json={
            "email": email,
            "password": password
        })

        try:
            content = response.json()
        except ValueError:
            return JsonResponse({
                "error": "Invalid response from Ayor backend.",
                "raw": response.text
            }, status=500)

        if response.status_code == 200:
            return JsonResponse(content, status=200)
        else:
            return JsonResponse(content, status=response.status_code)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
def refresh_view(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST method allowed"}, status=405)

    try:
        data = json.loads(request.body)
        refresh = data.get("refresh")

        if not refresh:
            return JsonResponse({"error": "Refresh token is required."}, status=400)

        response = requests.post(f"{BASE_URL}/auth/jwt/refresh/", json={
            "refresh": refresh
        })

        try:
            content = response.json()
        except ValueError:
            return JsonResponse({
                "error": "Invalid response from Ayor backend.",
                "raw": response.text
            }, status=500)

        if response.status_code == 200:
            return JsonResponse(content, status=200)
        else:
            return JsonResponse(content, status=response.status_code)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
