from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request,"index.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['Username']


 
    return render(request,"welcome.html",{'username':username})

