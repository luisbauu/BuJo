from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import home, profile, key, this_week, today

def page_home(request): 
	form = home()
	# if request.method == 'POST':
	# 	form = home(request.POST)
	# else:
	# 	form = home()
	return render(request, 'home.html', {'form' : form})

def page_profile(request):
	return render(request, 'profile.html',{'profile': profile})

def page_key(request):
	return render(request, 'key.html',{'profile': profile})

def page_this_week(request):
	return render(request, 'this_week.html',{'profile': profile})

def page_today(request):
	return render(request, 'today.html',{'profile': profile})
