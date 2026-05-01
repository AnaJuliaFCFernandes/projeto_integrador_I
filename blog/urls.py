from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('os/<int:pk>/', views.os_detail, name='os_detail'),
    path('os/nova/', views.os_nova, name='os_nova'),
    path('os/<int:pk>/edit/', views.os_edit, name='os_edit'),
]