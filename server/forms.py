from django import forms 
from .models import Server, Profile


class ServerForm(forms.ModelForm):
    class Meta:
        model = Server
        fields = ['server_name', 'version', 'ip', 'description', 'number_of_players', 'server_status', 'server_owner']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [ 'biography', 'date_of_birth', 'city']        