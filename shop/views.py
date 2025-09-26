from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Flower, Order
from .serializers import FlowerSerializer, OrderSerializer

 
@api_view(['GET'])
def api_flower_list(request):
    flowers = Flower.objects.all()
    serializer = FlowerSerializer(flowers, many=True)
    return Response(serializer.data)

 
@api_view(['GET'])
def api_flower_detail(request, flower_id):
    flower = get_object_or_404(Flower, id=flower_id)
    serializer = FlowerSerializer(flower)
    return Response(serializer.data)

 
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_buy_flower(request, flower_id):
    flower = get_object_or_404(Flower, id=flower_id)
    if flower.quantity < 1:
        return Response({'error': 'Out of stock'}, status=400)
    order = Order.objects.create(user=request.user, flower=flower)
    flower.quantity -= 1
    flower.save()
    serializer = OrderSerializer(order)
    return Response(serializer.data)

 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_order_history(request):
    orders = Order.objects.filter(user=request.user)
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)