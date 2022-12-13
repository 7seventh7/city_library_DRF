import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from catalog.models import *


# class BookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = ('title', 'author', 'year_of_writing')

# class BookModel:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    author = serializers.CharField()
    summary = serializers.CharField(max_length=1000)
    genre = serializers.CharField()
    year_of_writing = serializers.IntegerField()
    #photo = models.ImageField(upload_to="photo/%Y/%m/%d/", verbose_name='Фото')

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

class PersonSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Person
        fields = ('__all__')

# class PersonSerializer(serializers.Serializer):
#     name = serializers.CharField()
#     age = serializers.IntegerField()
#     time_creation = serializers.DateTimeField(read_only=True)
#
#     def create(self, validated_data):
#         return Person.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.age = validated_data.get('age', instance.age)
#         instance.time_create = timezone.now()#validated_data.get('time_create', instance.time_create)
#         instance.save()
#         return instance

# def encode():
#     model = BookModel('Властелин колец', 'Толкин')
#     model_sr = BookSerializer(model)
#     print(model_sr, type(model_sr), end='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Vlastelin colec","author":"Tolkin"}')
#     data = JSONParser().parse(stream)
#     print(data, type(data), end='\n')
#     serializer = BookSerializer(data=data)
#     print(serializer, end='\n')
#     serializer.is_valid()
#     print(serializer.validated_data)