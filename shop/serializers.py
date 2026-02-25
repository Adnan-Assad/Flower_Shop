from rest_framework import serializers
from .models import Flower, Order

class FlowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flower
        fields = ['id','title', 'description', 'category','price', 'image' ]

class OrderSerializer(serializers.ModelSerializer):
    flower = FlowerSerializer()   
    class Meta:
        model = Order
        fields = ['user', 'flower', 'quantity','status', 'ordered_at']