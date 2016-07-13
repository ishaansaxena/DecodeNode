from __future__ import unicode_literals

from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models
from decode.models import Level


class UserData(models.Model):
    user = models.OneToOneField(User, related_name='details', on_delete=models.CASCADE)
    current_level = models.ForeignKey(Level, default=Level.objects.get(pk=1).pk)
    current_level_time = models.DateTimeField(default=timezone.now)
    profile_picture = models.ImageField(upload_to='static/assets/user_images/', blank=True)
    is_banned = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def set_level(self, level_id):
        self.current_level = Level.objects.get(pk=level_id)
        self.current_level_time = timezone.now()


def create_user_data(sender, instance, created, **kwargs):  
    if created:  
       profile, created = UserData.objects.get_or_create(user=instance)  

post_save.connect(create_user_data, User) 
        