from rest_framework import generics

from apps.movie.models import Genre, Movie
from apps.movie.serializers import (
    MovieSerializer,
    GenreListCreateSerializer,
    GenreDetailSerializer
)
from core.permissions.common_permissions import IsAdminOrReadOnly


class GenreListCreateView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreListCreateSerializer
    permissions_classes = (IsAdminOrReadOnly,)


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    lookup_url_kwarg = 'genre_id'
    queryset = Genre.objects.all()
    serializer_class = GenreDetailSerializer
    permissions_classes = (IsAdminOrReadOnly,)


class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permissions_classes = (IsAdminOrReadOnly,)


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permissions_classes = (IsAdminOrReadOnly,)
    lookup_url_kwarg = 'movie_id'

