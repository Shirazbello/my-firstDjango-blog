from django.urls import path
from . import views
#Adding our URL Patterns for our Created Blogs

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]