from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def home(request):
    return render(request,'posts/home.html')


def contact(request):
    return render(request,'posts/contact.html')

def education(request):
    return render(request,'posts/Education.html')

def projects(request):
    return render(request,'posts/projects.html')

def skills(request):
    return render(request,'posts/skills.html')

def resume(request):
    return render(request,'posts/resume.html')

def certificates_achievements(request):
    return render(request,'posts/certificates_achievements.html')

def ms0(request):
    return render(request,'posts/marksheet.html',{"ms":0})

def ms1(request):
    return render(request,'posts/marksheet.html',{"ms":1})

def ms2(request):
    return render(request,'posts/marksheet.html',{"ms":2})

def ms6(request):
    return render(request,'posts/marksheet.html',{"ms":6})

def ms7(request):
    return render(request,'posts/marksheet.html',{"ms":7})

def ms8(request):
    return render(request,'posts/marksheet.html',{"ms":8})

def ms9(request):
    return render(request,'posts/marksheet.html',{"ms":9})


