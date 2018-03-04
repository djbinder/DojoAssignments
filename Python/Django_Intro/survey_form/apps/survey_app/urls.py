from django.conf.urls import url, include
from . import views      


urlpatterns = [
        url(r'^$', views.index),
        url(r'^survey_app/process$', views.process),
        url(r'^results$', views.results)
]


# urlpatterns = [
#     url(r'^$',views.index),
#     url(r'^surveys/process$', views.process),
#     url(r'^result$', views.result),
# ]