from django.shortcuts import render, render_to_response

# Create your views here.

class Person(object):
   def __init__(self, name, age, sex):
	self.name = name
	self.age = age
	self.sex = sex
	
   def say(self):
	return "I'm " + self.name



def index(req):
    #user = {'name':'yuens', 'age':23, 'sex':'male'}
    user = Person('zhm', 23, 'male')
    book_list = ['python', 'java', 'php', 'web']

    return render_to_response('index.html', {'title': 'index_title', 'user': user, 'book_list': book_list})
