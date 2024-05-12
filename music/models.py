from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=50)
    image = models.URLField()

    class Meta:
        ordering = ["id"]
        indexes = [
            models.Index(fields=['id'])
        ]


class Albom(models.Model):
    title = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True, blank=True)
    cover = models.URLField(null=True)
    last_update = models.DateField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        indexes = [
            models.Index(fields=['id'])
        ]


class Songs(models.Model):
    title = models.CharField(max_length=50)
    cover = models.URLField(null=True)
    albom = models.ForeignKey(Albom, on_delete=models.CASCADE, null=True, blank=True)
    listened = models.PositiveIntegerField(default=0)
    last_update = models.DateField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        indexes = [
            models.Index(fields=['id'])
        ]
