from django.conf.urls import url
from . import views      

urlpatterns = [
        url(r'^$', views.index),
        url(r'^createuser$', views.createuser),
        url(r'^login$', views.login),
        url(r'^show$', views.show),
        url(r'^createappointment$', views.createappointment),
        url(r'^edit/(?P<id>\d+)$', views.edit),
        url(r'^update/(?P<id>\d+)$', views.update),
        url(r'^destroy/(?P<id>\d+)$', views.destroy),
        url(r'^(?P<id>\d+)/delete$', views.delete),
        url(r'^logout$', views.logout),
]

# url(r'^(?P<id>\d+)/destroy$', views.destroy),  




