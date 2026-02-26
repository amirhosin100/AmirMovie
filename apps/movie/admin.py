from django.contrib import admin
from base.base_admin import BaseAdmin

from apps.movie.models import Genre, Movie


@admin.register(Movie)
class MovieAdmin(BaseAdmin):
    list_display = ('title',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('title',)