from django.urls import path
from .views import BookListView, BookCreateView, BookDeleteView, BookDetailView, AddReviewView, BookUpdateView

app_name = 'books'

urlpatterns = [
    path('book-list/', BookListView.as_view(), name='book_list'),
    path('book-detail/<int:pk>', BookDetailView.as_view(), name='book_detail'),
    path('delete/<int:pk>', BookDeleteView.as_view(), name='book_delete'),
    path('create/', BookCreateView.as_view(), name='book_create'),
    path('add_review/<int:pk>', AddReviewView.as_view(), name='add_review'),
    path('update/<int:pk>', BookUpdateView.as_view(), name='update' )
]
