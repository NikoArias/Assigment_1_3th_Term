from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/register', views.register_api_endpoint, name='register_api_endpoint'),
    path('api/login', views.login_api_endpoint, name='login_api_endpoint'),
    path('api/music', views.list_create_music_api_endpoint, name='list_create_music_api_endpoint'),
    path('api/rud/<id>', views.comments_rud_api_endpoint, name='comments_rud_api_endpoint'),
]
