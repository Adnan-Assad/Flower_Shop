from django.urls import path
from . import views

urlpatterns = [
    path('api/flowers/', views.api_flower_list, name='api_flower_list'),
    path('api/flowers/<int:flower_id>/', views.api_flower_detail, name='api_flower_detail'),
    path('api/buy/<int:flower_id>/', views.api_buy_flower, name='api_buy_flower'),
    path('api/orders/', views.api_order_history, name='api_order'),
]