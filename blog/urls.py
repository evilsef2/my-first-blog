# -*- coding: utf-8 -*-
from django.conf.urls import url

from blog.views import PostsListView, PostDetailView 
from . import views

urlpatterns = [
	url(r'^$', PostsListView.as_view(), name='list'), # то есть по URL http://имя_сайта/blognew/ 
                                               # будет выводиться список постов
	url(r'^(?P<pk>\d+)/$', PostDetailView.as_view()), # а по URL http://имя_сайта/blognew/число/ 
                                              # будет выводиться пост с определенным номером
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	
]