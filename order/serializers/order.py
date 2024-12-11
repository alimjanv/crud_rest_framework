from rest_framework import serializers
from ..models.order import Order

class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'customer', 'order_date', 'status', 'price']