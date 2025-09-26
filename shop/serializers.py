from rest_framework import serializers
from .models import Flower, Order

class FlowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flower
        fields = ['title', 'description', 'category' ]

class OrderSerializer(serializers.ModelSerializer):
    flower = FlowerSerializer()   
    class Meta:
        model = Order
        fields = ['user', 'flwoer', 'quantity','status']