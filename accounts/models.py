from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone

class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError('Users must have an username.')
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            date_joined=timezone.now()
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            username,
            email,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
        

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=32, verbose_name='username', unique=True, default='anonymau5')
    email = models.EmailField(verbose_name='email address', unique=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_admin = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def save(self, *args, **kwargs):
        if self.pk is None:
            super(User, self).save(*args, **kwargs)
            details = UserDetails(user=self)
            details.save()
        else:
            super(User, self).save(*args, **kwargs)

class UserDetails(models.Model):
    user = models.OneToOneField(User, related_name='details')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    current_level = models.IntegerField(default=0)
    current_level_time = models.DateTimeField(default=timezone.now)
    profile_picture = models.ImageField(upload_to='static/assets/user_images/')
