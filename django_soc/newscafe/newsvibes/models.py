from django.db import models

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
