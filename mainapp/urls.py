from django.urls import path

from mainapp import views


urlpatterns = [
    path('',views.index, name='index'),
    path('login_user',views.login_user,name='login_user'),
    path('signup',views.signup,name='signup'),
]