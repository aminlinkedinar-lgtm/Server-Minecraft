from django.db import models
from django.conf import settings

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