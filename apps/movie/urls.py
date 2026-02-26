from django.urls import path
from .views import (
    GenreListCreateView,
    GenreRetrieveUpdateDestroyView,
    MovieRetrieveUpdateDestroyView,
    MovieListCreateView
)

app_name = 'movie'

urlpatterns = [
    path(
        'list/',
        MovieListCreateView.as_view(http_method_names=['get']),
        name='list-create'
    ),
    path(
        'create/',
        MovieListCreateView.as_view(http_method_names=['post']),
        name='create',
    ),
    path(
        '<str:movie_id>/update/',
        MovieRetrieveUpdateDestroyView.as_view(http_method_names=['put', 'patch']),
    ),
    path(
        '<str:movie_id>/delete/',
        MovieRetrieveUpdateDestroyView.as_view(http_method_names=['delete']),
    ),
    path(
        '<str:movie_id>/retrieve/',
        MovieRetrieveUpdateDestroyView.as_view(http_method_names=['get']),
    ),

    # Genre
    path(
        'genre/list/',
        GenreListCreateView.as_view(http_method_names=['get']),
        name='genre-list'
    ),
    path(
        'genre/create/',
        GenreListCreateView.as_view(http_method_names=['post']),
        name='genre-list'
    ),
    path(
        'genre/<str:movie_id>/update/',
        GenreRetrieveUpdateDestroyView.as_view(http_method_names=['put', 'patch']),
        name='genre-list'
    ),
    path(
        'genre/<str:movie_id>/delete/',
        GenreRetrieveUpdateDestroyView.as_view(http_method_names=['delete']),
        name='genre-list'
    ),
    path(
        'genre/<str:movie_id>/retrieve/',
        GenreRetrieveUpdateDestroyView.as_view(http_method_names=['get']),
        name='genre-list'
    ),
]
