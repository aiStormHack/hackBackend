from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import requests
from decouple import config

BASE_URL = config("BASE_URL")


@method_decorator(csrf_exempt, name='dispatch')
class DashboardStatsView(View):
    def get(self, request, shop_id):
        try:
            access_token = request.headers.get("Authorization")
            if not access_token:
                access_token = request.GET.get("access")

            if not access_token:
                return JsonResponse({"error": "Access token is required."}, status=401)

            if access_token.startswith("Bearer "):
                access_token = access_token.split("Bearer ")[-1]

            url = f"{BASE_URL}/api/shops/{shop_id}/dashboard-stats/"
            headers = {"Authorization": f"Bearer {access_token}"}

            response = requests.get(url, headers=headers)

            return JsonResponse(
                response.json() if response.status_code == 200 else {
                    "error": "Failed to fetch dashboard stats",
                    "status_code": response.status_code,
                    "response": response.text  
                },
                status=response.status_code
            )
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

