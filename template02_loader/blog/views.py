from django.shortcuts import render, render_to_response

# method 1 import 
#from django.http import HttpResponse
#from django.template import loader, Context

# Create your views here.

## method 1
'''
def index(req):
    t = loader.get_template('index.html')
    c = Context({})

    return HttpResponse(t.render(c))
'''


## method 2
def index(req):
    return render_to_response('index.html', {})
