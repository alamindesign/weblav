from django.shortcuts import render,redirect
from . import models
from . import forms
# Create your views here.
def studenthome(request):
    all_student = models.Students.objects.all()
    all_programs = models.Program.objects.all()
    return render(request,'studentApp\index.html',{'Students':all_student,'Programs': all_programs})
def remove(request,id):
    student = models.Students.objects.get(id = id)
    student.delete()
    return redirect(studenthome)
def addnewstudent(request):
    stf = forms.StudentForm()
    return render(request,'studentApp/addnewstudent.html',{'stf':stf})
def savestudent(request):
    if request.method == "POST":
        sform = forms.StudentForm(request.POST)
        if sform.is_valid():
            try:
                sform.save
            except:
                pass
            return redirect(studenthome)