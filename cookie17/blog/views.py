from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django import forms

# Create your views here.

def UserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

def register(request):
    if request.method == "POST":
	uf = UserForm(request.POST)
	if uf.is_valid():
	    username = uf.cleaned_data['username']
	    password = uf.cleaned_data['password']
	    print username, password
	    return HttpResponse("ok")
    else:
	uf = UserForm()
    return render_to_response("register.html", {'uf': uf})

