from django.urls import path
from .views import DashboardStatsView  

urlpatterns = [
    path('api/shops/<uuid:shop_id>/dashboard-stats/', DashboardStatsView.as_view(), name='dashboard_stats'),
]
