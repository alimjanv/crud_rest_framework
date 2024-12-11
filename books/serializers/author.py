from rest_framework import serializers
from ..models.author import Author



class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name', 'surname', 'age')
