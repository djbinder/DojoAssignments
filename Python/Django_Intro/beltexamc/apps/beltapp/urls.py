from django.conf.urls import url
from . import views      

urlpatterns = [
    url(r'^$', views.index),
    url(r'^createuser$', views.createuser),
    url(r'^login$', views.login),
    url(r'^home$', views.home),
    url(r'^addfavorite/(?P<id>\d+)$', views.addfavorite),
    url(r'^removefavorite/(?P<id>\d+)$', views.removefavorite),
    url(r'^addquote$', views.addquote),
    url(r'^users/(?P<id>\d+)$', views.users),
    url(r'^logout$', views.logout),
]



# urlpatterns = [
#     url(r'^$', views.index),
#     url(r'^register$', views.register),
#     url(r'^login$', views.login),
#     url(r'^success$', views.success),
#     url(r'^logout$', views.logout),
#     url(r'^new$', views.new),
#     url(r'^create$', views.create),
#     url(r'^(?P<id>\d+)/favorite$', views.favorite),
#     url(r'^(?P<id>\d+)/popback$', views.popback),
#     url(r'^(?P<id>\d+)/show$', views.show),
#     url(r'^(?P<id>\d+)/remove$', views.remove),
#     url(r'^(?P<id>\d+)/delete$', views.destroy),
# ]

# urlpatterns = [
#         url(r'^$', views.index),
#         url(r'^createuser$', views.createuser),
#         url(r'^login$', views.login),
#         url(r'^viewdashboard$', views.viewdashboard),
#         url(r'^viewadditem$', views.viewadditem),
#         url(r'^additem$', views.additem),
#         url(r'^addwish/(?P<id>\d+)$', views.addwish),
#         url(r'^removewish/(?P<id>\d+)$', views.removewish),
#         url(r'^allwishers/(?P<id>\d+)$', views.allwishers),
#         url(r'^destroy/(?P<id>\d+)$', views.destroy),
#         url(r'^logout$', views.logout),
# ]