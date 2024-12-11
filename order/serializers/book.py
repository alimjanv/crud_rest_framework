from rest_framework import serializers
from ..models.book import OrderBook


class OrderBookSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderBook
        fields = ['title','subtitle', 'author_id', 'price']
