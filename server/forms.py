from django import forms 
from .models import Server


class ServerForm(forms.ModelForm):
    class Meta:
        model = Server
        fields = ['server_name', 'version', 'ip', 'description', 'number_of_players', 'server_status', 'server_owner']