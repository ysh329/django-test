from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django import forms
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os

# Create your views here.

class UserForm(forms.Form):
   username = forms.CharField()
   rawFile = forms.FileField() 


def register(request):
    if request.method == "POST":
	uf = UserForm(request.POST, request.FILES)
	if uf.is_valid():
	    print uf.cleaned_data['username']
	    print request.FILES
	    raw_file_name = uf.cleaned_data['rawFile'].name
	    raw_file_size = uf.cleaned_data['rawFile'].size
	    print '+++++++++++++++++++++'
	    print "raw_file_size:%s" % raw_file_size
	    print '+++++++++++++++++++++'
	    print os.getcwd()
	    print '+++++++++++++++++++++'
	    try:
		f = open('./upload/' + raw_file_name, 'w')
		f.write(uf.cleaned_data['rawFile'].read())
	    except Exception as e:
		print e
	    finally:
		f.close()

	    return HttpResponse(str(uf.cleaned_data) + 'ok')

    else:
        uf = UserForm()

    return render_to_response('register.html', {'uf': uf})


