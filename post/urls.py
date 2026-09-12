from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_posts, name='all_posts'),
    path('create', views.create_posts, name='create_posts'),
    path('<int:post_id>/', views.single_post, name='single_post'),
    path('register/', views.register, name='register'),
    path('<int:post_id>/edit/', views.edit_post, name='edit_post'),
    path('<int:post_id>/delete/', views.delete_post, name='delete_post')
]
