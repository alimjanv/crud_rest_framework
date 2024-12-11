from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    customer = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=50, choices=[("Pending", "Pending"), ("Shipped", "Shipped"), ("Completed", "Completed")])
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id}"
