from django.db import models

# Create your models here.
class Students(models.Model):
    student_id = models.SmallIntegerField()
    student_name = models.CharField(max_length=30)
    district = models.CharField(max_length=20)
    cell_no = models.CharField(max_length=11)
    email = models.EmailField()
    doB = models.DateField()
    program_name = models.ForeignKey('Program' , on_delete=models.CASCADE)
    def __int__(self):
        return self.student_id
class Program(models.Model):
    program_name = models.CharField(max_length=30)

    def __str__(self):
        return self.program_name