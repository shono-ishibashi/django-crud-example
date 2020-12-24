from django.urls import path
from . import views


urlpatterns = [
    path('', views.list, name='list'),
    path('new/', views.new, name='new'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('<int:post_id>/edit/', views.edit, name='edit'),
]
