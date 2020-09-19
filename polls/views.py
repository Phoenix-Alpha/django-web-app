from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Student

def index(request):
    return HttpResponse("Hello, world. You are at the polls index.")

# def student_show(request):
#     x = []
#     for i in range(10):
#         x.append(i)
#     return HttpResponse("<h1>Django Tutorial</h1>The digits are {0}".format(x))

def student_show(request):
    student = Student.objects.order_by('roll_no')
    return render(request, 'student/student_show.html', {'student': student})

