from django.contrib import admin
from shop.models import Flower, Order

# Register your models here.
@admin.register(Flower)
class FlowerAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'quantity')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'flower', 'quantity', 'status', 'ordered_at')
    list_filter = ('status',)

