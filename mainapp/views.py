from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request,"index.html")

def login_user(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['password']
        user = authenticate(request,username=username,password= password)
        if user is not None:
            login(request,user)            
            return render(request,"welcome.html",{'username':username})
        else:
            return redirect('index')


def signup(request):
  
    if request.method == 'POST':
        username = request.POST['uname']
        email = request.POST['mail']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            user = User.objects.create_user(username=username,email=email,password= password1)
            user.save()
            return redirect('index')
    return render(request,"signup.html")     


