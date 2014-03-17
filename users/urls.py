from django.conf.urls import patterns, url

from users import views

urlpatterns = patterns('',
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^register/$', views.user_register, name='user_register'),
)