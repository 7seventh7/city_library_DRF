from django.shortcuts import render

from catalog.serializer import BookSerializer
from .models import *
from rest_framework import generics

class BooksAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


