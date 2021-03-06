"""firstapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url



urlpatterns = [
    url(r'^1/', ('article.views.basic_one')),
    url(r'^2/', ('article.views.template_two')),
    url(r'^3/', ('article.views.template_three')),

#blog
    url(r'^articles/all/$', 'article.views.articles'),
    url(r'^articles/get/(?P<article_id>\d+)/$', 'article.views.article'), #show one article on the html page
    url(r'^articles/addlike/(?P<article_id>\d+)/$', 'article.views.addlike'), #add likes
    url(r'^articles/adddislike/(?P<article_id>\d+)/$', 'article.views.adddislike'), #add likes
    url(r'^articles/addcomment/(?P<article_id>\d+)/$', 'article.views.addcomment'), #add comments
    url(r'^page/(\d+)/$', 'article.views.articles'),
    #url(r'^page/(?P<pg>\d+)/$', 'article.views.articles'),
    url(r'^', 'article.views.articles'),
    #url(r'^', 'ArticleListView.as_view()'),    
] 
