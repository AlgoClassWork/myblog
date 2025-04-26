from django.urls import path 
from . import views

urlpatterns = [
    path('', views.post_list , name='post_list'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('post/<int:id>/share/', views.post_share, name='post_share'),
]
