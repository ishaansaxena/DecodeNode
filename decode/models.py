from __future__ import unicode_literals
from django.db import models


class Level(models.Model):
    uid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=250)
    image = models.ImageField(default=None, blank=True)
    comment = models.CharField(max_length=200)
    answer = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return str(self.uid)

    @classmethod
    def set_default(self):
        self.default_uid = 1
        self.default_level = self(uid=self.default_uid)
        self.default_pk = 1
        self.default_level.pk = self.default_pk       
        self.default_level.save()

    @classmethod
    def get_default(self):
        try:
            return self.default_level
        except AttributeError:
            self.set_default()
            return self.default_level