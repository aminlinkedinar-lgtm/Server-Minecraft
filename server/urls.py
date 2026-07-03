from django.urls import path 
from .views import *

urlpatterns = [
    path("", home_server_viwe, name='home'),
    path("server-list/", server_list_viwe, name='server_list'),
    path('add-server/', add_server_viwe, name='add_server'),
    path('server-information/', server_information_viwe, name='server_information'),
    path('delete-server/', delete_server_viwe, name='delete_server'),
    path('server/update/<int:id>/', update_server_viwe, name='update_server'),
    path('register/', register_server_viwe, name='register_server'),
    path('profile/', profile_server_viwe, name = 'profile'),
    path('add_profile/',create_profile_viwe, name = 'create_profile'),
    path('edit-profile/', edit_profile_viwe, name = 'edit_profile'),
    ]
