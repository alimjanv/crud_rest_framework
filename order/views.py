from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import render

from .models.order import Order
from .models.order_item import OrderItem
from .serializers.order import OrderSerializers
from .serializers.order_item import OrderItemSerializers



class OrderAPIView(APIView):
    authenticate_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request, pk):
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response({"detail": "Order not found."}, status=status.HTTP_404_NOT_FOUND)

        order_serializer = OrderSerializers(order)
        return Response(order_serializer.data)

    def post(self, request):
        order_serializer = OrderSerializers(data=request.data)
        if order_serializer.is_valid():
            order_serializer.save()
            return Response(order_serializer.data, status=status.HTTP_201_CREATED)
        return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def put(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        serializer = OrderSerializers(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderItemDetailAPIView(APIView):
    def get(self, request, order_pk, item_pk):
        try:
            order_item = OrderItem.objects.get(order__id=order_pk, id=item_pk)
        except OrderItem.DoesNotExist:
            return Response({"detail": "Order item not found."}, status=status.HTTP_404_NOT_FOUND)

        order_item_serializer = OrderItemSerializers(order_item)
        return Response(order_item_serializer.data)

    def post(self, request, order_pk):
        order = get_object_or_404(Order, pk=order_pk)
        serializer = OrderItemSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(order=order)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, order_pk, item_pk):
        order_item = get_object_or_404(OrderItem, order__id=order_pk, id=item_pk)
        serializer = OrderItemSerializers(order_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, order_pk, item_pk):
        order_item = get_object_or_404(OrderItem, order__id=order_pk, id=item_pk)
        order_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

