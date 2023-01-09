from django.shortcuts import render, redirect
from .models import Course
# Create your views here.
# def edit(request):
#     return render()
def home(request):
    all_courses = Course.objects.all()
    return render(request,'courseApp\index.html',{'courses': all_courses});
def remove(request,id):
    course = Course.objects.get(id = id)
    course.delete()
    return redirect(home)

