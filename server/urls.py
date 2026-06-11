from django.urls import path 
from .views import home_server_viwe, server_list_viwe

urlpatterns = [
    path("", home_server_viwe, name='home'),
    path("server-list/", server_list_viwe, name='server_list'),
]
