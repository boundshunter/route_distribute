from django.db import models

# Create your models here.
# app01 userinfo


class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    gender = models.CharField(max_length=10)
    age = models.CharField(max_length=10)