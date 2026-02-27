from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',view=views.home,name="home"),
    path('login/',view=views.login,name="login"),
    path('signup/',views.signup,name="signup")
]
