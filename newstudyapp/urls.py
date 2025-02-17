from django.urls import path
from.import  views
urlpatterns=[path("",views.home,name="home"),
             path("path1",views.about,name="about")]