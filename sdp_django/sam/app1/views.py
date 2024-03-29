from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login,logout
from .models import products


# from .forms import CreateUserForm
# from .models import User


# Create your views here.
def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')



def home(request):
    if request.method == "POST":
        username = request.POST['userid']
        passwd = request.POST['password']
        user = authenticate(request, username=username, password=passwd)
        if user is not None:
            # pro=products.objects.all()
            auth_login(request, user)
            return render(request, 'home.html')
        else:
            messages.info(request, 'invalid')
            return redirect('/login')
    # return HttpResponse("hi")


def register(request):
    return render(request, 'registration.html')


def verify(request):
    if request.method == "POST":

        first_name = request.POST['fname']
        last_name = request.POST['lname']
        # mobile=request.POST['mobile']
        mail = request.POST['email_id']
        passwd = request.POST['password']
        if not (User.objects.filter(username=first_name).exists()):
            user = User.objects.create_user(username=first_name, password=passwd, email=mail, first_name=first_name,
                                            last_name=last_name)
            user.save()
            return render(request, 'login.html')
        else:
            messages.info(request, 'User name taken')
            print("wrong bruh")
            return redirect('/newuser')

    # return HttpResponse('verified')


def profile(request):
    context = {
        'user': request.user
    }
    return render(request, 'profile.html', context)
def user_logout(request):
    logout(request)
    return redirect('/login')
