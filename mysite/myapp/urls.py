from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
urlpatterns = [
    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.user_login,name='login'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('html/',views.html,name='html'),
    path('css/',views.css,name='css'),
    path('js/',views.js,name='js'),
    path('django/',views.dj,name='django'),
    path('python/',views.python,name='python'),
    path('invalid/',views.Invalid,name='invalid'),
    path('logout/',auth_view.LogoutView.as_view(template_name='myapp/logout.html'),name='logout'),
]
