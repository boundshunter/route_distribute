from django.shortcuts import render,HttpResponse,redirect
# from django.shortcuts import
from app01 import models
# Create your views here.


def login(request):
    print(request.method)
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        print(u,p)
        obj = models.UserInfo.objects.filter(username=u, password=p).first()
        if obj:
            return redirect("/app01/index/")
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')


def index(request):
    return render(request, 'index.html')


def user_info(request):
    if request.method == 'GET':
        user_list = models.UserInfo.objects.all()
        return render(request, 'user_info.html', {'user_list': user_list})
    elif request.method == 'POST':
        u = request.POST.get('uname')
        p = request.POST.get('pwd')
        ge = request.POST.get('gender')
        ag = request.POST.get('age')
        models.UserInfo.objects.create(username=u, password=p, gender=ge, age=ag)
        return redirect('/app01/user_info/')


def user_group(request):
    pass


def user_detail(request, nid):
    # return HttpResponse(nid)
    obj = models.UserInfo.objects.filter(id=nid).first()

    # 取单挑数据，如果不存在直接报错， models.UserInfo.objects.get(id=nid),所以此方法需要 try
    return render(request,'user_detail.html', {"obj": obj})


def user_del(request, nid):
    models.UserInfo.objects.filter(id=nid).first().delete()
    return redirect('/app01/user_info')


def user_edit(request, nid):
    if request.method == 'GET':
        obj = models.UserInfo.objects.filter(id=nid).first()
        return render(request, 'user_edit.html', {'obj': obj})
    elif request.method == 'POST':
        nid = request.POST.get('id')
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        g = request.POST.get('gend')
        a = request.POST.get('age')
        models.UserInfo.objects.filter(id=nid).update(username=u, password=p, gender=g, age=a)
        return redirect('/app01/user_info/')

def orm(request):
    # 创建数据 推荐使用 1,2
    # 1.
    models.UserInfo.objects.create(username='jfsu', password='abc123', gender='男', age='28')
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