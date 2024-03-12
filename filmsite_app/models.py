from django.db import models
from pytils.translit import slugify

class Genre(models.Model):
    name = models.CharField("Name", max_length=255)
    slug = models.SlugField(unique=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Film(models.Model):
    name = models.CharField("Name", max_length=255)
    director = models.CharField("Director", max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name="Genre")
    rating = models.FloatField("Rating")
    description = models.TextField("Description")
    url_poster = models.CharField("URL Poster", max_length=500)
    url_banner = models.CharField("URL Banner", max_length=500)
    url_film = models.CharField("URL Film", max_length=500)
    is_top_ten = models.BooleanField("Is top 10", null=True, blank=True)

    def __str__(self):
        return self.name