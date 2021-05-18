from django.shortcuts import render

# Create your views here.
import json

def home(request):
    return render(request,'home/index.html');

def DistrictWise(request,state):
    return render(request,'home/DistrictWise.html',{'state':state});