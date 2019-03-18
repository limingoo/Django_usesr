from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from app.models import User

# 进入登录页面
def login(request):
    return render(request,"login.html")

# 进入注册页面
def registe(request):
    return render(request,"regist.html")

# 执行注册操作，把注册页面的数据进行获取，并存入数据库
def doRegiste(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    sex=request.POST.get("sex")
    age=request.POST.get("age")
    user=User.objects.create(username=username,password=password,sex=sex,age=age)
    return render(request,"regist_success.html")

# 执行登录操作，判断用户名密码是否正确
def doLogin(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    #select * from users where username = "zhangsan" and password = "123123"
    user=User.objects.filter(Q(username=username)&Q(password=password)).first()
    if user:
        # 登录成功进入登录成功页面
        return render(request,"login_success.html",context={"user":user.username})
    else:
        # 登录失败继续进入登录页面
        return render(request,"login.html",context={"msg":"用户名或者密码错误！！！","username":username})

#查询全部
def index(request):
    users=User.objects.all()
    return render(request,"user_manager.html",context={"users":users})

#修改用户
#进入修改页面，先查询要修改的用户，把用户信息展示在修改页面
def updateUser(request):
    id=request.GET.get("id")
    user=User.objects.filter(id=id).last()
    return render(request,"user_edit.html",context={"user":user})

# 做用户的修改处理，底层语句为
# update users set username="wangwu",password="111",sex="女",age=50 where id=1
def doUpdateUser(request):
    id=request.POST.get("id")
    uname=request.POST.get("uname")
    pwd=request.POST.get("pwd")
    age=request.POST.get("age")
    sex=request.POST.get("sex")
    # 根据查询要修改的用户
    user=User.objects.filter(id=id).last()
    # 修改原本数据库中的值
    user.username=uname
    user.password=pwd
    user.age=age
    user.sex=sex
    user.save() #执行修改操作
    # 重定向到主页
    return HttpResponseRedirect("/index/")

# 执行删除操作
def delUser(request):
    id = request.GET.get("id")
    user=User.objects.filter(id=id).last()
    user.delete()
    return HttpResponseRedirect("/index/")