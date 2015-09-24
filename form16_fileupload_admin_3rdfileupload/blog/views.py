from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django import forms
from blog.models import User


# Create your views here.

class UserForm(forms.Form):
    username = forms.CharField()
    headImg = forms.FileField()

def register(request):
    if request.method == "POST":
	uf = UserForm(request.POST, request.FILES)
	if uf.is_valid():
	    print uf.cleaned_data
	    username = uf.cleaned_data['username']
	    headImg = uf.cleaned_data['headImg']
	    print username, headImg

	    user = User()
	    user.username = username
	    user.headImg = headImg
	    user.save()

	    return HttpResponse("ok")
    else:
	uf = UserForm()
    return render_to_response('register.html', {'uf': uf})
