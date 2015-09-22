"""djproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

# method 2
#from blog.views import index



urlpatterns = [
    # method 3 (current version not support)
    #'blog.views',

    url(r'^admin/', include(admin.site.urls)),

    # method 2	
    #url(r'^blog/index/$', index),

    # method 3 (current version not support)
    #url(r'^blog/index/$', 'index'),

    # defined name
    #url(r'^blog/index/(?P<id>\d{2})/$', 'blog.views.index')

    # no defined name
    url(r'^blog/index/(\d{2})/$', 'blog.views.index'),
]
