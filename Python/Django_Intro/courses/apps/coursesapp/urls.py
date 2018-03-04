from django.conf.urls import url
from . import views  

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^login$', views.login, name='login'),
        url(r'^courses$', views.show, name='show_courses'),
        url(r'^createuser$', views.createuser, name='create_user'),
        url(r'^createcourse$', views.createcourse, name='create_course'),
        url(r'^profile/$', views.profile, name='view_profile'),
        url(r'^profile/(?P<id>\d+)$', views.profile, name='view_profile'),
        url(r'^favorite/(?P<id>\d+)$', views.favorite),
        url(r'^unfavorite/(?P<id>\d+)$', views.unfavorite),
        url(r'^destroy/(?P<id>\d+)$', views.destroy),  
        url(r'^delete/(?P<id>\d+)$', views.delete),
        url(r'^logout$', views.logout),
]

# url(r'^(?P<id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
# url(r'^favorites/(?P<userid>\d+)$', views.favorite),
        # url(r'^favorite/(?P<id>\d+)$', views.favorite),


# urlpatterns = [
#     url(r'^(?P<id>\d+)/delete$', views.delete, name='delete'),
#     url(r'^(?P<id>\d+)/addFaves$', views.addFaves, name='addFaves'),
#     url(r'^(?P<id>\d+)/profile$', views.profile, name='profile'),
#     url(r'^(?P<id>\d+)/destroy$', views.destroy, name='destroy'),
#     url(r'^(?P<id>\d+)/unfave$', views.unfave, name='unfave'),
# ]