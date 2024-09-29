from django.urls import path
from .views import BookViewSet,AuthorViewSet,CategoryViewSet

urlpatterns = [
    path('book', BookViewSet.as_view({
        'get': 'list',
        'post': 'post'
    })),
    path('author', AuthorViewSet.as_view({
        'get': 'list',
        'post': 'post'
    })),
    path('category', CategoryViewSet.as_view({
        'get': 'list',
        'post': 'post'
    })),
]