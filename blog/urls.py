from django.urls import path

from . import views


urlpatterns = [
    path('', views.blog_index, name='blog'),
    path('post/<int:pk>/', views.post_details, name='post_details'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]