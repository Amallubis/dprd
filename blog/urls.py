from django.urls import path,re_path 
from . import views
app_name ='blog'
urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^post/(?P<slugInput>[\w-]+)/$', views.article_detail),
    re_path(r'^catagory/(?P<catagoryInput>[\w-]+)/$', views.catagory),
] 