from django.contrib import admin
from .models.author import Author
from .models.book import Book
# Register your models here.

admin.site.register(Book)
admin.site.register(Author)

