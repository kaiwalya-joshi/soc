from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class NEWS(models.Model):
    title = models.CharField(max_length=1000, default=None, null=True)
    description = models.CharField(max_length=10000, default=None, null=True)
    Newsurl = models.CharField(max_length=10000, default=None, null=True)
    Imageurl = models.CharField(max_length=10000, default=None, null=True)
    publishedAt = models.CharField(max_length=1000, default=None, null=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, default=None)
    password = models.CharField(max_length = 100, default=None)
    token = models.CharField(max_length=10)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

