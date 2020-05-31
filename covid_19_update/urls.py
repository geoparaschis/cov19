from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$', views.index, name='index'),
url('news/', views.show_articles, name='news'),
url('tweets/', views.show_tweets, name='tweets'),
url('login/', views.login, name='login'),
]