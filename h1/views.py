from django import http
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
# Create your views here.
def index(request):
    stu = Student.objects.all() 
    return render(request, 'index.html', {'data':stu}) 

def form(request):
    if request.method == 'POST':
        name = request.POST.get('name') 
        roll = request.POST.get('roll')
        reg = request.POST.get('reg')
        dep = request.POST.get('dep') 
        details = Student(name=name,roll=roll,reg=reg,dep=dep)
        details.save()
        # return HttpResponse("your account has been created") 
    stu = Student.objects.all() 
    return render(request, 'index.html',{'data':stu}) 

def delete(request,id):
    if request.method == 'POST':
        data=Student.objects.get(pk=id) 
        data.delete() 
    return HttpResponseRedirect('/') 