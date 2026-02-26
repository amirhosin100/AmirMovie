from django.db import models
from base.base_model import BaseModel


class Genre(models.Model):
    title = models.CharField(
        max_length=255,
    )

    class Meta:
        indexes = [
            models.Index(fields=['title'])
        ]

    def __str__(self):
        return self.title


class Movie(BaseModel):
    title = models.CharField(
        max_length=255,
    )
    genres = models.ManyToManyField(
        Genre,
        related_name='movies',
    )
    description = models.TextField(
        max_length=4000,
        blank=True,
        null=True,
    )
    poster = models.ImageField(
        upload_to='movies/posters',
    )

    class Meta:
        ordering = ('-created_at',)

        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['-created_at']),
        ]

    def __str__(self):
        return self.title
