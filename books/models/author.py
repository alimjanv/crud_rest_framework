from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=40)
    age = models.IntegerField()
    email = models.EmailField()


    def __str__(self):
        return f"{self. name} {self.surname}"