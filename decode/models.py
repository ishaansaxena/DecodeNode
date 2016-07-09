from __future__ import unicode_literals
from django.db import models


class Level(models.Model):
    uid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=250)
    image = models.SlugField(default=None)
    comment = models.CharField(max_length=200)
    answer = models.TextField(max_length=50)

    def __str__(self):
        return str(self.uid) + u" - " + self.title
