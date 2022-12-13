
from django.contrib import admin
from django.urls import path, include, re_path

from catalog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
   #path('api/v1/bookslist/', BooksAPIView.as_view()),
    path('api/v1/personlist/', PersonAPIList.as_view()),
    path('api/v1/personlist/<int:pk>/', PersonAPIUpdate.as_view()),
    path('api/v1/persondelete/<int:pk>/', PersonAPIDestroy.as_view()),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
