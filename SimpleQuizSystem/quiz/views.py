from django.shortcuts import render
from quiz.models import Exam, Examlog
from django.shortcuts import redirect


# Create your views here.

'''def home(request):
    exam = Exam.objects.all()
    return render(request, "index.html", {"exam": exam})'''
   
def register(request):
    return render(request, "register.html")

def reg(request):
    usename = request.POST['text']
    user_password = request.POST['text1']
    data = Examlog(Name=usename, password=user_password)
    data.save()
    return render(request, "login.html")

def login(request):
    return render(request, "login.html")

def log(request):
    usename = request.POST['text']
    user_password = request.POST['text1']
    data = Examlog.objects.get(Name=usename, password=user_password)
    request.session['member_id'] = data.id
    exam = Exam.objects.all()
    return render(request, "index.html", {"exam": exam})
    

