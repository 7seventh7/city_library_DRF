
from django.contrib import admin
from django.urls import path

from catalog.views import BooksAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/bookslist/', BooksAPIView.as_view())
]
