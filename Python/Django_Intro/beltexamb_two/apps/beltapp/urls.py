from django.conf.urls import url
from . import views      

urlpatterns = [
        url(r'^$', views.index),
        url(r'^createuser$', views.createuser),
        url(r'^login$', views.login),
        url(r'^viewdashboard$', views.viewdashboard),
        url(r'^viewadditem$', views.viewadditem),
        url(r'^additem$', views.additem),
        url(r'^addwish/(?P<id>\d+)$', views.addwish),
        url(r'^removewish/(?P<id>\d+)$', views.removewish),
        url(r'^allwishers/(?P<id>\d+)$', views.allwishers),
        url(r'^destroy/(?P<id>\d+)$', views.destroy),
        url(r'^logout$', views.logout),
]