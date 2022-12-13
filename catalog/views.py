from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone

from catalog.serializer import BookSerializer, PersonSerializer
from .models import *
from rest_framework import generics

# class BooksAPIView(APIView):
#
#     def get(self, request):
#         w = Book.objects.all()
#         return Response({'booooks': BookSerializer(w, many=True).data})
#
#     # def post(self, request):
#     #     serializer = BookSerializer(data=request.data)
#     #     serializer.is_valid(raise_exception=True)
#     #     serializer.save()
#
#
#         return Response({'post': serializer.data})

class PersonAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer




class PersonAPIList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class PersonAPIDestroy(generics.DestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = (IsAdminUser, )
class PersonAPIView(APIView):

    def get(self, request):
        w = Person.objects.all()
        return Response({'person': PersonSerializer(w, many=True).data})

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()


        return Response({'person': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({'error': 'Method PUT not allowed'})
        try:
            instance = Person.objects.get(pk=pk)
        except:
            return Response({'error': 'Method PUT not allowed'})


        serializer = PersonSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})