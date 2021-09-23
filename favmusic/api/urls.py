from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register_api_endpoint, name='register_api_endpoint'),
    path('login', views.login_api_endpoint, name='login_api_endpoint'),
    path('music', views.list_create_music_api_endpoint, name='list_create_music_api_endpoint'),
    path('rud/<id>', views.comments_rud_api_endpoint, name='comments_rud_api_endpoint'),
]
