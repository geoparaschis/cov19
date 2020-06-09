from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^news/$', views.show_articles, name='news'),
url(r'^tweets/$', views.show_tweets, name='tweets'),
url(r'^login/$', views.login, name='login'),
url(r'^covid-19/$', views.covid, name='covid-19'),
url(r'^(?P<area_id>[0-9]+)/$', views.area_data, name='popup'),
url(r'^(?P<area_id>[0-9]+)/$', views.area_data, name='pharm'),
]