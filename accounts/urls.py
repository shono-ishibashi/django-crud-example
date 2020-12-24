from django.urls import path

from . import views

app_name = 'account'

urlpatterns = [
    path('register/', views.CreateAccount.as_view(), name='resister'),
    path('login/', views.LoginAccount.as_view(), name='login'),
]
