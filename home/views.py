import datetime
from django.shortcuts import render
#DataFlair #Views #TemplateInheritance
def home(request):
    context = {'k2' : 'Welcome to the Second Page'}
    return render(request, 'home/base.html', context)

def other(request):
    context = {'k1': 'Welcome to the Second page', }
    return render(request, 'home/others.html', context)

def about(request):
    time = datetime.datetime.now()
    return render(request, 'home/about.html',{'time': time})