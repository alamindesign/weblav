from django.db import models

# Create your models here.
class Course (models.Model):
    course_id= models.CharField(max_length=20)
    course_name = models.CharField(max_length=50)
    course_credit = models.DecimalField(decimal_places=2,max_length=10,max_digits=5)
    ct_full_marks = models.DecimalField(decimal_places=2,max_length=10,max_digits=5)
    mid_full_marks = models.DecimalField(decimal_places=2,max_length=10,max_digits=5)
    att_full_marks = models.DecimalField(decimal_places=2,max_length=10,max_digits=5)
    final_full_marks = models.DecimalField(decimal_places=2,max_length=10,max_digits=5)
