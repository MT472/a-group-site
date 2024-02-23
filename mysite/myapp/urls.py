from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/',views.register,name='signup'),
    path('',views.index,name='index'),
    path('login/',views.user_login,name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('html/',views.html,name='html'),
    path('css/',views.css,name='css'),
    path('js/',views.js,name='js'),
    path('django/',views.dj,name='django'),
    path('python/',views.python,name='python'),
    path('invalid/',views.Invalid,name='invalid')
]
