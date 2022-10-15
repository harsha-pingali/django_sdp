from django.shortcuts import render
from django.http import HttpResponse


# views used for request -response
# Create your views here.

def index(request):
    return render(request,'index.html')


def home(request):
    return render(request, 'space_login.html')



