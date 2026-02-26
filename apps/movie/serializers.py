from rest_framework import serializers

from apps.movie.models import Genre, Movie


class GenreListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = (
            'title',
            'id'
        )
        read_only_fields = ('id',)


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreListCreateSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = (
            'id',
            'title',
            'poster',
            'genres',
            'description',
        )
        read_only_fields = ('id',)


class GenreDetailSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = Genre
        fields = (
            'title',
            'movies',
            'id'
        )
        read_only_fields = ('id',)
