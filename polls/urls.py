from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student', views.student_show, name='student_show')
]