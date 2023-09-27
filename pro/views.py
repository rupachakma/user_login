from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User

def homep(request):
    return render(request,"home.html")

def loginp(request):
    return render(request,"login.html")
   
def signupp(request):
    if request.method=="POST":
        un=request.POST.get("username")
        em=request.POST.get("email")
        pas1=request.POST.get("password1")
        pas2=request.POST.get("password2")
        if pas1!=pas2:
            return HttpResponse("Not Match")
        else:
            # myu=User.objects.create_user(un,em,pas1)
            # myu.save()
            return redirect("loginp")


    return render(request,"signup.html")
   