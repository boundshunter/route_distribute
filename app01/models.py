from django.db import models

# Create your models here.
# app01 userinfo


class UserGroup(models.Model):
    uid = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=32,unique=True)
    ctime = models.DateTimeField(auto_now_add=True,null=True)
    uptime = models.DateTimeField(auto_now=True,null=True)



class UserInfo(models.Model):
    #id列，自增，逐渐
    #用户名列，字符串类型，指定长度
    #字符串，数字，时间，二进制
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    gender = models.CharField(max_length=10)
    age = models.CharField(max_length=10)
    user_group = models.ForeignKey("UserGroup", to_field='uid', default=1, on_delete=models.CASCADE)
    user_type_choices = (
        (1,'超级用户'),
        (2,'普通用户'),
        (3,'临时用户'),
    )
    user_type_id = models.IntegerField(choices=user_type_choices, default=1)
