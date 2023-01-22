from django.urls import path
from . import views
urlpatterns = [
    path('', views.studenthome, name='student' ),
    path('del/<int:id>', views.remove, name='remove'),
    path('addnewstudent', views.addnewstudent , name='addnewstudent'),
    path('save', views.savestudent, name="saveStudent")
]