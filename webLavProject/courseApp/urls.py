from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="homepage"),
    path('del/<int:id>', views.remove, name='delete'),
    path('addnew/', views.addNewCourse, name="addNewCourse"),
    path('save/', views.save , name="save"),
    path('edit/<int:id>', views.edit , name="edit"),
    path('update/<int:id>', views.update, name="update")
]