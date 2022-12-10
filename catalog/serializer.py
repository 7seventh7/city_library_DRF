from rest_framework import serializers

from catalog.models import *


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'author', 'year_of_writing')