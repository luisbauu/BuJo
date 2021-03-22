from django.shortcuts import render
from django.http import HttpResponse
from .forms import home

def index(request): 
	form = home()
	return render(request,'profile.html',{'home' : home})

