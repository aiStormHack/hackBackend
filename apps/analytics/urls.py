from django.urls import path

from .views.dashboard_stats_view import DashboardStatsView 
from .views.order_status_count_view import OrderStatusCountView 
from .views.general_stats_view import GeneralStatsView
from .views.top_sales_view import TopSalesView
from .views.orders_analytics_view import OrdersAnalyticsView

urlpatterns = [
    path('api/shops/<uuid:shop_id>/dashboard-stats/', DashboardStatsView.as_view(), name='dashboard_stats'),
    path('api/shops/<uuid:shop_id>/order-status-count/', OrderStatusCountView.as_view(), name='order_status_count'),  
    path('api/shops/<uuid:shop_id>/analytics/general-stats/', GeneralStatsView.as_view(), name='general_stats'),
    path('api/shops/<uuid:shop_id>/analytics/top-sales/', TopSalesView.as_view(), name='top_sales'),
    path('api/shops/<uuid:shop_id>/analytics/orders/', OrdersAnalyticsView.as_view(), name='orders_analytics')
    
]
