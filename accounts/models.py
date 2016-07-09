from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class UserData(models.Model):
    user = models.OneToOneField(User, related_name='details', on_delete=models.CASCADE)
    current_level = models.IntegerField(default=0)
    current_level_time = models.DateTimeField(default=timezone.now)
    profile_picture = models.ImageField(upload_to='static/assets/user_images/')

    def __str__(self):
        return self.user.username