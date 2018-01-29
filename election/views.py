from  django.http import *
from  django.shortcuts import render
from django.contrib.auth import authenticate, login

def home(request):

        profile = request.session["email"]
        return  render(request, 'index.html', {'profile':profile})


def login_error(request):
    return  render(request,'login_error.html')


def login_view(request):
    if request.method == "POST":
        email=request.POST["email"]
        password=request.POST["password"]
        user=authenticate(request, username=email, password=password)
        #data= "%s, %s" % (username, password)
        if user is not None:
            login(request, user)
            request.session["email"]=email
            return render(request, 'index.html')
        else:
            return render(request, 'login_error.html')

    else:
        return  render(request, 'login_view.html')
