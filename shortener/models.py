from django.db import models
from django.db.models import CASCADE
from django.contrib.auth.models import User

# Create your models here.


class Person(models.Model):
    user = models.OneToOneField(User, null=True,blank=True, on_delete=CASCADE)
    profile_pic = models.ImageField(null=True, blank=True, default='1.jpeg')
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class URLS(models.Model):
    long_url = models.URLField(max_length=200)
    short_url = models.URLField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE ,null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.short_url
