from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from catalog.serializer import BookSerializer
from .models import *
from rest_framework import generics

class BooksAPIView(APIView):

    def get(self, request):
        w = Book.objects.all()
        return Response({'booooks': BookSerializer(w, many=True).data})

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()


        return Response({'post': serializer.data})
