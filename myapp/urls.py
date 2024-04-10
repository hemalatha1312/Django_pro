from django.urls import path
from .views import BookListView
from myapp.views import add_book

urlpatterns = [
    path('', BookListView.as_view(), name='book-list'),
    path('add/',add_book, name='add-book'),
]