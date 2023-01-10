from django.shortcuts import render, redirect
from .models import Course
from .forms import CourseForm
# Create your views here.
def home(request):
    all_courses = Course.objects.all()
    return render(request,'courseApp\index.html',{'courses': all_courses});
def remove(request,id):
    course = Course.objects.get(id = id)
    course.delete()
    return redirect(home)
def addNewCourse(request):
    frm = CourseForm()
    return render(request,'courseApp/addnewcourse.html',{'cfrom': frm})
def save(request):
    if request.method=="POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                pass
    return redirect(home)
def edit(request,id):
    edt = Course.objects.get(id = id)
    editform = CourseForm(instance=edt)
    return render(request,'courseApp/edit.html',{'editform':editform})
