from django.db import models

class URL(models.Model):
    hash = models.CharField(max_length=10, unique=True)
    url = models.URLField()
    visits = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.url
