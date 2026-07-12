from django import forms 
from .models import Server, Profile


class ServerForm(forms.ModelForm):
    class Meta:
        model = Server
        fields = ['server_name', 
                  'version', 
                  'ip', 
                  'description', 
                  'number_of_players', 
                  'server_status']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
                "profile_picture",
                'first_name', 
                'last_name', 
                'phone_number', 
                'biography', 
                'date_of_birth', 
                'city']        