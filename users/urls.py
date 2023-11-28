from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from reservejá import settings
from . import views


urlpatterns = [

    path('login/', views.login_request, name='login'),
    path('register', views.register, name='register'),
    path('account', views.account, name='account'),
    path('logout', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout')

]

