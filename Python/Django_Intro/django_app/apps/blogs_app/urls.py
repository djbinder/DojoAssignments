#DJANGO_APP
# LITTLE URLs

from django.conf.urls import url, include
from . import views      
urlpatterns = [
    url(r'^$', views.index), 
    url(r'^new$', views.new),   
    url(r'^create$', views.create),
    url(r'^(?P<number>\d+)$', views.show),
    url(r'^(?P<number>\d+)/edit/$', views.edit),
    url(r'^(?P<number>\d+)/delete/$', views.destroy)
]




# url(r'^(?P<id>\d+)$', views.show)
# url(r'^edit/(?P<id>\d+)$', views.edit)