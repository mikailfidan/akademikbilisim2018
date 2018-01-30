from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from election.profile.models import UserProfile
from election.models import Survey


def home(request):

     items=Survey.objects.all()
     return render(request,'index.html', {'items':items})


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
            return home(request)

        else:
            return login_error(request)

   else:
        return  render(request, 'login_view.html')


def logout_view(request):
    logout(request)
    return redirect ("/login_view/")


def signup_view(request):

    if request.method == "POST":

        email = request.POST["email"]
        name = request.POST["name"]
        password = request.POST["password"]
        passwordverify=request.POST["password-verify"]
        user=UserProfile.objects.filter(email=email).exists()

        if user is True:
            hata="Bu email zaten kayıtlı"
            return render(request, 'signup_view.html', {'hata':hata})

        else:

            if password == passwordverify:
                user=UserProfile(email=email, name=name, password=password, is_active=True)
                user.set_password(password)
                user.save()
                scs="Kayıt İşlemi Başarılı"
                return render(request, 'signup_view.html', {'scs': scs})

            else:
                hatapasswd="Parola alanları aynı değil"
                return render(request, 'signup_view.html', {'hatapasswd': hatapasswd})

    else:
        return render(request, 'signup_view.html')