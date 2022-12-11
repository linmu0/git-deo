from django.shortcuts import render
import pymysql
from app01 import function_

from django.http import HttpResponse

Mysql_operate=function_.Mysql_operate()

def home(request):
    return render(request, "home.html")

def add(request):
    if request.method=='GET':
        return render(request,"add.html")
    name=request.POST.get("stuname")
    id=request.POST.get("id")
    stuphone=request.POST.get("stuphone")
    adress=request.POST.get("adress")
    point=request.POST.get("point")
    high=request.POST.get("high")
    Mysql_operate.stu_Insert(account,id,name,stuphone,point,high,adress)
    return  render(request,"add.html",{"error_msg":"添加成功"})


def delete(request):
    if request.method == 'GET':
        return render(request,"delete.html")
    id=request.POST.get("id")
    Mysql_operate.Delete(id,account)
    return  render(request,"delete.html",{"error_msg":"删除成功"})


def update(request):
    if request.method == 'GET':
        return render(request,"update.html")
    id_old=request.POST.get('id_old')
    name=request.POST.get("stuname")
    id=request.POST.get("id")
    stuphone=request.POST.get("stuphone")
    address=request.POST.get("adress")
    point=request.POST.get("point")
    high=request.POST.get("high")
    Mysql_operate.Update_stu(account,id_old,id,name,stuphone,point,high,address)
    return  render(request,"update.html",{"error_msg":"修改成功"})
# 登录
def Login(request):
    if request.method == 'GET':
        return render(request,"login.html")
    global account
    account  = request.POST.get("account")
    password = request.POST.get("password")
    # 判断账号密码是否正确
    status=Mysql_operate.account_password_Comparison(account,password)
    if status:
        return render(request,"home.html")
    return render(request,"login.html",{"error_msg":"账号或密码错误"})
def sort(request):
    if request.method == 'GET':
        return render(request,"sort.html")
    choose=request.POST.get("choose")
    if choose=='学分':
        choose=3
    else:
        choose=4
    #输出排序顺序
    data=function_.sort_stu(account,choose)
    return render(request, "sort.html", {"list": data.lis})
def Inquire(request):
    if request.method == 'GET':
        data = Mysql_operate.All_data_stu(account)
        return render(request, "Inquire.html", {"list": list(data)})
    choose=request.POST.get("choose")
    keyword = request.POST.get('keyword')
    if choose=='学号':
        result = Mysql_operate.All_data_stu(account)
        data = function_.search(result,int(keyword)).data
        data=(data,)
        return render(request, "Inquire.html", {"list": list(data)})
    elif choose=='姓名':
        choose=1
    elif choose=='电话':
        choose=2
    elif choose=='平均绩点':
        choose=3
    elif choose=='身高':
        choose=4
    else:
        choose=5
    data = list(Mysql_operate.All_data_stu(account))
    data=function_.BST(data,keyword,choose).result
    return render(request, "Inquire.html", {"list": list(data)})

def updatePassword(request):
    if request.method == 'GET':
        return render(request,'updatePassword.html')
    Account = request.POST.get("account")
    old_password = request.POST.get("old_password")
    new_password = request.POST.get("new_password")
    # 判断账号密码是否正确
    status = Mysql_operate.account_password_Comparison(Account, old_password)
    if status:
        Mysql_operate.Update_account(Account,new_password)
        return render(request, "updatePassword.html",{"error_msg": "密码修改成功"})
    return render(request, "updatePassword.html", {"error_msg": "账号或密码错误"})
def enroll(request):
    if request.method == 'GET':
        return render(request,'enroll.html')
    Account  = request.POST.get("account")
    password = request.POST.get("password")
    # 判断账号是否存在
    status=Mysql_operate.account_judgment(Account)
    if status:
        # 创建账号
        Mysql_operate.account_Insert(Account,password)
        # 创建对应表格
        Mysql_operate.student_information_creat(Account)
        return render(request,"enroll.html",{"error_msg":"注册成功"})
    return render(request,"enroll.html",{"error_msg":"账号或密码错误"})


