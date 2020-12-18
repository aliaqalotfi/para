from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.http import Http404
from django.shortcuts import render, redirect
from . import models


# Create your views here.
def register_page(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        re_password=request.POST.get("re_password")
        if password == re_password:
            User.objects.create_user(username=username,password=password)
        else: raise Http404("pass word doesnot match")

    context={}
    return render(request,"account_sys/register_page.html",context)




def login_page(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        login(request,user)



    context={}
    return render(request,"account_sys/login_page.html",context)





def log_out(request):
    logout(request)
    return redirect("/")




def profile(request):
    username=request.user.username
    user=User.objects.get(username=username)
    profile=models.UserPhoto.objects.get(user=user)



    context={
        "profile":profile
    }
    return render(request, "account_sys/profile.html", context)