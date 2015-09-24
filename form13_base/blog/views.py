from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django import forms

# Create your views here.

class UserForm(forms.Form):
    name = forms.CharField()
    


def register(request):
    if request.method == 'POST':
	form = UserForm(request.POST)
	if form.is_valid():
	    print form.cleaned_data
	    return HttpResponse(str(form.cleaned_data) + 'ok')
    else:
	form = UserForm()
    return render_to_response('register.html', {'form': form})



