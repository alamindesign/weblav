from django.shortcuts import render,redirect
from . import models
# Create your views here.
def home(request):
    all_student = models.Students.objects.all()
    all_programs = models.Program.objects.all()
    return render(request,'studentApp\index.html',{'Students':all_student,'Programs': all_programs})
def remove(request,id):
    student = models.Students.objects.get(id = id)
    student.delete()
    return redirect(home)