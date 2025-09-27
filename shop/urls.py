from django.urls import path
from . import views

urlpatterns = [
    path('flowers/', views.api_flower_list, name='api_flower_list'),
    path('flowers/<int:flower_id>/', views.api_flower_detail, name='api_flower_detail'),
    path('buy/<int:flower_id>/', views.api_buy_flower, name='api_buy_flower'),
    path('orders/', views.api_order_history, name='api_order'),
]