
from .views import OrderAPIView, OrderItemDetailAPIView
from django.urls import path


urlpatterns = [
    path('order', OrderAPIView.as_view(), name='list-create'),
    path('order/<int:pk>', OrderAPIView.as_view(), name='update-delete'),
    path('order_items', OrderItemDetailAPIView.as_view(), name='list-create'),
    path('order_items/<int:pk>', OrderItemDetailAPIView.as_view(), name='update-delete')


]

