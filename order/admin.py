from django.contrib import admin
from .models.order import Order
from .models.author import Author
from .models.book import Book
from .models.order_item import OrderItem
# Register your models here.
admin.site.register(Order)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(OrderItem)

