from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import requests
from decouple import config

BASE_URL = config("BASE_URL")


@method_decorator(csrf_exempt, name='dispatch')
class GeneralStatsView(View):
    def get(self, request, shop_id):
        try:
            access_token = request.headers.get("Authorization")
            if not access_token:
                access_token = request.GET.get("access")

            if not access_token:
                return JsonResponse({"error": "Access token is required."}, status=401)

            if access_token.startswith("Bearer "):
                access_token = access_token.split("Bearer ")[-1]

            start_date = request.GET.get("start_date")
            end_date = request.GET.get("end_date")

            if not start_date or not end_date:
                return JsonResponse({"error": "start_date and end_date are required."}, status=400)

            url = f"{BASE_URL}/api/shops/{shop_id}/analytics/general-stats/"
            params = {
                "start_date": start_date,
                "end_date": end_date
            }
            headers = {"Authorization": f"Bearer {access_token}"}

            response = requests.get(url, headers=headers, params=params)

            return JsonResponse(
                response.json() if response.status_code == 200 else {
                    "error": "Failed to fetch general stats",
                    "status_code": response.status_code,
                    "response": response.text
                },
                status=response.status_code
            )
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
