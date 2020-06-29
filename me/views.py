from django.shortcuts import render,redirect
from .models import One
# Create your views here.


def resume(request):
    abt=One.objects.all()
    return render(request,'resume.html',{'abt':abt})