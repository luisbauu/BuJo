from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from datetime import datetime
from .forms import home, profile, key, this_week, today

def page_home(request): 
	if request.method == 'POST':
		form = home(request.POST)
		if form.is_valid():
			return render(request, 'home.html', {'form' : form, 'name' : form.cleaned_data['name']})
	else:
		form = home()
		return render(request, 'home.html', {'form' : form})

def page_profile(request):
	return render(request, 'profile.html')

def page_key(request):
	return render(request, 'key.html')

def page_this_week(request):
    return render(request, 'this_week.html')

def page_today(request):

    myDate = datetime.now()
    formattedDate = myDate.strftime("%m.%d.%A")
    
    return render(request, 'today.html', {'date': formattedDate})
