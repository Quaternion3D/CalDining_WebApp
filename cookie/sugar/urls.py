from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^main/$', views.main, name='main'),
    url(r'^login/$', views.login, name='main'),
    url(r'^auth/$', views.auth_view, name='main'),
    url(r'^logout/$', views.logout, name='main'),
    url(r'^loggedin/$', views.loggedin, name='main'),
    url(r'^invalid/$', views.invalid_login, name='main'),
    url(r'^update_favs/$', views.invalid_login, name='main'),

]