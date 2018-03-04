from django.conf.urls import url
from . import views     


urlpatterns = [
        url(r'^$', views.index),
        url(r'^createuser$', views.createuser),
        url(r'^login$', views.login),
        url(r'dashboard$', views.dashboard),
        url(r'^show/(?P<id>\d+)$', views.show),
        url(r'^wish/(?P<id>\d+)$', views.wish),
        url(r'^wishers$', views.viewwishers),
        url(r'^wishers/(?P<id>\d+)$', views.viewwishers),
        url(r'^createitem$', views.createitem),
        url(r'^createitemview$', views.createitemview),
        url(r'^destroy/(?P<id>\d+)$', views.destroy),
        url(r'^delete/(?P<id>\d+)$', views.delete),
        url(r'^logout$', views.logout),
]