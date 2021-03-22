from django import forms

class home(forms.Form):
	name = forms.CharField(label='', max_length = 25)
