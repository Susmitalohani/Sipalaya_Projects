from django.shortcuts import render
from datetime import datetime
from .models import guest
from django.http import HttpResponse

# Create your views here.
def index(request):
    current=datetime.now().year
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        messages=request.POST['messages']

        form=guest(name=name,email=email,phone=phone,messages=messages)
        form.save()
        return HttpResponse("Successfully send!!!")
    return render(request,'index.html',{'date':current})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def menu(request):
    return render(request,'menu.html')

def services(request):
    return render(request,'services.html')