from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *


# Create your views here.
def index(req):
  tasks=Task.objects.all()
  form=TaskForm()
  if req.method=="POST":
    form=TaskForm(req.POST)
    if form.is_valid():
      form.save()
    return redirect('/')
  context={'tasks':tasks,'form':form}
  return render(req,'task/list.html',context)

def updateTask(req,pk):
  task=Task.objects.get(id=pk)
  form=TaskForm(instance=task)
  context={'form':form}
 
  if req.method=="POST":
    form=TaskForm(req.POST,instance=task)
    if form.is_valid():
      form.save()
    return redirect('/')
  return render(req,'task/update.html',context)

def deleteTask(req,pk):
  item=Task.objects.get(id=pk)
  if req.method=="POST":
    item.delete()
    return redirect('/')
  context={'item':item}
  return render(req,'task/delete.html',context)
  
