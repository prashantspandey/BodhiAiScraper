from django.conf.urls import url

from . import views

app_name = 'home'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^article/(?P<slug>[\w-]+)/$', views.individual_post, name='detail'),
    url(r'^sports-news/$',views.sports_section,name='sports_section'),
    url(r'^world-news/$',views.worldNews_section,name='worldNews_section'),
    url(r'^india-news/$',views.indiaNews_section,name='indiaNews_section'),
    url(r'^entertainment-movies-news/$',views.movies_section,name='movies_section'),
    url(r'^science-tech/$',views.scienceandtech_section,name='scienceandtech_section'),

]
