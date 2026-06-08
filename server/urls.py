from django.urls import path 
from .views import home_server_viwe

urlpatterns = [
    path("", home_server_viwe, name='home'),
]
