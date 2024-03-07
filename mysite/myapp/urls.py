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
    path('logout/',views.user_logout,name='logout'),
    path('password_change/',auth_view.PasswordChangeView.as_view(template_name='myapp/change_password.html'),name='password_change'),
    path('password_change/done/',auth_view.PasswordChangeDoneView.as_view(template_name='myapp/change_password_done.html'),name='password_change_done'),
    path('password_reset/',auth_view.PasswordResetView.as_view(template_name='myapp/password_reset.html'),name='password_reset'),
    path('password_reset/done/',auth_view.PasswordResetDoneView.as_view(template_name='myapp/password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>',auth_view.PasswordResetConfirmView.as_view(template_name='myapp/password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset/done/',auth_view.PasswordResetCompleteView.as_view(template_name='myapp/password_reset_complete.html'),name='password_reset_complete'),
]
