from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.


class Server(models.Model):
    server_name = models.CharField(max_length=50)
    version = models.CharField( max_length=50)
    ip = models.GenericIPAddressField()
    description = models.TextField()
    number_of_players = models.IntegerField(default=0)
    server_status = models.BooleanField()
    creation_data = models.DateTimeField(auto_now_add=True)
    server_owner  = models.ForeignKey( settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    def __str__(self):
        return self.server_name

class Profile(models.Model):
    user = models.OneToOneField(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE)
    # profile_picture = models.ImageField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)
    biography = models.TextField()
    date_of_birth = models.DateTimeField()
    city = models.DateTimeField()
     