from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY_CHOICES =[
    ('Rose', 'Rose'),
    ('Tulip', 'Tulip'),
    ('Lily', 'Lily'),
    ('Orchid', 'Orchid')
]

class Flower(models.Model):
    title = models.TextField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='flowers/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    quantity = models.PositiveIntegerField(default=10)

    def __str__(self):
        return self.title
    
class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.flower.title}"

