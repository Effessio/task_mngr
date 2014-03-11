# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from projects import views
from django.views.generic import TemplateView

urlpatterns = patterns(
    '',
    #(r'^$', TemplateView.as_view(template_name="projects/index.html")),
    url(r'^$', views.index, name='index'),
)
