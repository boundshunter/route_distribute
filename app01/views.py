from django.shortcuts import render,HttpResponse,redirect
# from django.shortcuts import
from app01 import models
# Create your views here.


def login(request):
    return HttpResponse('app01 login access')


def orm(request):
    # 创建数据 推荐使用 1,2
    # 1.
    # models.UserInfo.objects.create(username='jfsu', password='abc123', gender='男', age='28')
    # 2.
    # dic = {'username': 'alex', 'password': '123', 'gender': '女', 'age': '38'}
    # models.UserInfo.objects.create(**dic)
    # 3.
    # obj = models.UserInfo(username='abc', password='aaa', gender='女', age='20')
    # obj.save()

    # 删除数据
    # 删除表中所有数据
    # models.UserInfo.objects.all().delete()
    # 删除 指定条件数据
    # models.UserInfo.objects.filter(username='alex', age='38').delete()
    # models.UserInfo.objects.filter(id_gt=23).delete()

    # 查询
    # result = models.UserInfo.objects.all()
    result = models.UserInfo.objects.filter(username='alex')
    for row in result:
        print(row.username, row.password)

    # 修改
    # models.UserInfo.objects.filter(username='alex').update(username='alfx')
    models.UserInfo.objects.all().update(password='666')
    return HttpResponse('Orm DB Options')