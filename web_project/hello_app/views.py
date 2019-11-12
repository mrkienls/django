from django.shortcuts import render
import re
from datetime import datetime
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")

def hello_there(request, name):
    return render(
        request,
        'hello_app/hello_there.html',
        {
            'name':name,
            'date':datetime.now()
        }
    )
def home(request):
    return render(request, "hello_app/home.html")
def contact(request):
    return render(request, "hello_app/contact.html")
def about(request):
    return render(request, "hello_app/about.html")    

