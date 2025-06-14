from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    context={
        'data':tasks
    }
    return render(request, 'task_list.html',context )

def home(request):
    return render(request, 'home.html' )
def navbar(request):
    return render(request, 'nav.html' )

def base(request):
    return render(request, 'base.html' )

def contact(request):
    return render(request, 'contact.html' )

def about(request):
    return render(request, 'about.html' )