from django.urls import path 
from .views import home_server_viwe, server_list_viwe, add_server_viwe, server_information_viwe, delete_server_viwe

urlpatterns = [
    path("", home_server_viwe, name='home'),
    path("server-list/", server_list_viwe, name='server_list'),
    path('add-server/', add_server_viwe, name='add_server'),
    path('server-information/', server_information_viwe, name='server_information'),
    path('delete-server/', delete_server_viwe, name='delete_server'),
]
