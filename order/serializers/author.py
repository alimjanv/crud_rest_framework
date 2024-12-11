from rest_framework import serializers
from ..models.author import OrderAuthor

class OrderAuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderAuthor
        fields = ['name', 'email']
