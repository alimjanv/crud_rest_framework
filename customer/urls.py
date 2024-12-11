from django.urls import path
from .views import CustomerRetrieveAPIView


urlpatterns = [
    path('customer', CustomerRetrieveAPIView.as_view(), name='customer-create'),
    path('customer/<int:pk>', CustomerRetrieveAPIView.as_view(), name='customer-retrieve'),
]



