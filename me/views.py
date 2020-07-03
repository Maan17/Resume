from django.shortcuts import render,redirect
from .models import One,Career,Two_main,Two_explaination,Projects

# Create your views here.
def resume(request):
    abt=One.objects.all()
    career=Career.objects.all()
    two1=Two_main.objects.all()
    two2=Two_explaination.objects.all()
    project=Projects.objects.all()
    return render(request,'resume.html',{'abt':abt,'career':career,'two1':two1,'two2':two2,'project':project})