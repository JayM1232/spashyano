from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home_pg,name='homepage'),path('/photo-details/<int:pkimg>/',views.photo_detl,name='details'),path('/search-fields/',views.searching,name="serhbut"),path('/conatact-page/',views.contactadmin,name='cont')
]
