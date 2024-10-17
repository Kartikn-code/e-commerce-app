from django.shortcuts import render,redirect
from django.contrib import auth


# Create your views here.
def login(request):
    return render(request,"index.html",)
def help(request):
    return render (request,'help.html')
def authentication(request):
    print(request.method)
    if  request.method=="POST":
        username=request.POST.get('Username')
        password=request.POST.get('password')
        if username=="ping2karti2gmail.com" & password=="H@ppy2004":
            return redirect('mainpage')

def mainpage(request):
    return render(request,"mainpage.html")
def signin(request):
    return render(request,"signin.html")
def userentry(request):
    return render(request,"entry.html")