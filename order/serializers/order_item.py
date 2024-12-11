from rest_framework import serializers
from ..models.order_item import OrderItem

class OrderItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'user_id', 'status', 'order_date']
