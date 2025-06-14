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
