from django.urls import path
from .views import get_info, get_books, detail, add_books, update_books


urlpatterns = [
    path('', get_info, name="get_info"),
    path('books/<int:pk>', get_books, name="get_books"),
    path('books/detail/<int:pk>', detail, name="detail"),
    path('add_books/', add_books, name="add_books"),
    path('update/<int:pk>/', update_books, name="update_books"),
]