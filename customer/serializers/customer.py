from rest_framework import serializers
from ..models.customer import Customer


class CustomerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Customer
        fields = ['id', 'user', 'phone_number', 'address', 'is_verified']
