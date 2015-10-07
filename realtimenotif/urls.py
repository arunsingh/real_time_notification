"""realtimenotif URL Configuration

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
from sendnotif import views
#from sendnotif.views import home, alert

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
	
	#url(r'^/', include('realtimenotif.urls')),

	 #url(r'^$', 'sendnotif.views.home', name='home'),
	url(r'^$', views.home, name='home'),
	 #url(r'^alert/$', 'sendnotif.views.alert', name='alert'),
	url(r'^alert/$', views.alert, name='alert'),

	url(r'^accounts/login/$','django.contrib.auth.views.login',name='login'),
    
	#uncomment the next line to enable the admin:
    url(r'^admin/$', include(admin.site.urls)), 
]	
