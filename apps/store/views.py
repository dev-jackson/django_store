from django.shortcuts import render
from .models import User
# Create your views here.

def index(req):
    users = User.objects.all() #equals select * from User
    context = {
        'users': users
    }
    return render(req,'index.html',context)
