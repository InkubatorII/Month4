from django.db import models

class TVParser(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)

    def __str__(self):
        return self.title

